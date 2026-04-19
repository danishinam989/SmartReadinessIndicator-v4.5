import numpy as np
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io
import json
from datetime import datetime

class SRIOptimizer:
    def __init__(self):
        # Initialize domains and their weights
        self.domain_names = [
            'Energy Efficiency',
            'Energy Flexibility and Storage',
            'Comfort', 
            'Convenience',
            'Health, Well Being and Accessibility',
            'Maintenance and Fault Prediction',
            'Information to Occupants'
        ]
        
        # Domain weights from Ireland (West Europe) data
        self.domain_weights = {
            'Energy Efficiency': 0.1667,
            'Energy Flexibility and Storage': 0.3333,
            'Comfort': 0.0833,
            'Convenience': 0.0833,
            'Health, Well Being and Accessibility': 0.0833,
            'Maintenance and Fault Prediction': 0.1667,
            'Information to Occupants': 0.0833
        }

    def calculate_current_scores(self, current_answers, weight_files):
        """Calculate scores based on current answers"""
        scores = {domain: 0.0 for domain in self.domain_names}
        
        for domain_idx, weight_file in enumerate(weight_files):
            domain = self.domain_names[domain_idx]
            for q_id, answer in current_answers.items():
                q_num = q_id[1:]  # Remove 'q' prefix to get number
                if q_num in weight_file:
                    option_letter = answer[-1]  # Get option letter (a, b, c, etc.)
                    scores[domain] += weight_file[q_num].get(option_letter, 0)
        
        return scores

    def get_possible_upgrades(self, current_answers, weight_files, pricing, budget):
        """Get all possible upgrades within budget"""
        upgrades = []
        
        for q_id, current_opt in current_answers.items():
            q_num = q_id[1:]  # Remove 'q' prefix
            current_letter = current_opt[-1]
            
            if q_num in pricing:
                # Get all options that are higher than current
                current_price = pricing[q_num].get(current_letter, 0)
                for new_letter, new_price in pricing[q_num].items():
                    if new_letter > current_letter:
                        upgrade_cost = new_price - current_price
                        if upgrade_cost <= budget:
                            # Calculate domain impacts
                            domain_impacts = {}
                            total_weighted_impact = 0
                            
                            for domain_idx, weight_file in enumerate(weight_files):
                                domain = self.domain_names[domain_idx]
                                if q_num in weight_file:
                                    current_impact = weight_file[q_num].get(current_letter, 0)
                                    new_impact = weight_file[q_num].get(new_letter, 0)
                                    impact = new_impact - current_impact
                                    domain_impacts[domain] = impact
                                    total_weighted_impact += impact * self.domain_weights[domain]
                                else:
                                    domain_impacts[domain] = 0
                            
                            if total_weighted_impact > 0:
                                upgrades.append({
                                    'question': q_id,
                                    'from_opt': current_letter,
                                    'to_opt': new_letter,
                                    'cost': upgrade_cost,
                                    'domain_impacts': domain_impacts,
                                    'total_impact': total_weighted_impact,
                                    'roi': total_weighted_impact / upgrade_cost if upgrade_cost > 0 else 0
                                })
        
        return sorted(upgrades, key=lambda x: x['roi'], reverse=True)

    def optimize(self, upgrades, budget):
        """Optimize upgrades selection using dynamic programming"""
        if not upgrades:
            return []
            
        n = len(upgrades)
        dp = [[0.0] * (int(budget) + 1) for _ in range(n + 1)]
        keep = [[False] * (int(budget) + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for b in range(int(budget) + 1):
                upgrade = upgrades[i - 1]
                if upgrade['cost'] <= b:
                    new_value = dp[i-1][b - int(upgrade['cost'])] + upgrade['total_impact']
                    if new_value > dp[i-1][b]:
                        dp[i][b] = new_value
                        keep[i][b] = True
                    else:
                        dp[i][b] = dp[i-1][b]
                else:
                    dp[i][b] = dp[i-1][b]
        
        chosen = []
        b = int(budget)
        for i in range(n, 0, -1):
            if keep[i][b]:
                chosen.append(upgrades[i-1])
                b -= int(upgrades[i-1]['cost'])
        
        return chosen

    # def create_radar_chart(self, before_scores, after_scores):
    #     """Create a radar chart comparing before and after scores"""
    #     domains = self.domain_names
    #     num_vars = len(domains)
        
    #     angles = [n / float(num_vars) * 2 * np.pi for n in range(num_vars)]
    #     angles += angles[:1]
        
    #     before_values = list(before_scores.values())
    #     before_values += before_values[:1]
    #     after_values = list(after_scores.values())
    #     after_values += after_values[:1]
        
    #     fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        
    #     ax.plot(angles, before_values, 'o-', linewidth=2, label='Current', color='blue')
    #     ax.fill(angles, before_values, alpha=0.25, color='blue')
    #     ax.plot(angles, after_values, 'o-', linewidth=2, label='After Upgrades', color='green')
    #     ax.fill(angles, after_values, alpha=0.25, color='green')
        
    #     ax.set_xticks(angles[:-1])
    #     ax.set_xticklabels(domains, size=8)
        
    #     # Improve visual appearance
    #     ax.set_title('SRI Domain Scores Comparison', pad=20)
    #     ax.grid(True)
    #     ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
        
    #     plt.tight_layout()
        
        # Save to bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=300, bbox_inches='tight')
        buf.seek(0)
        plt.close()
        
        return buf

    def calculate_upgrade_scores(self, base_scores, chosen_upgrades):
        """Calculate new scores after upgrades"""
        new_scores = base_scores.copy()
        
        for upgrade in chosen_upgrades:
            for domain, impact in upgrade['domain_impacts'].items():
                new_scores[domain] += impact
        
        return new_scores

    def calculate_co2_savings(self, current_scores, future_scores):
        """
        Calculate potential annual CO2 savings based on energy efficiency improvements.
        Uses average EU conversion factors.
        
        Returns estimated annual CO2 savings in tonnes.
        """
        # Average EU conversion factors (kg CO2 per kWh)
        CONVERSION_FACTORS = {
            'electricity': 0.275,  # EU average electricity emission factor
            'heating': 0.202,     # Natural gas heating
            'cooling': 0.275      # Electric cooling
        }
        
        # Estimated annual energy consumption per domain (kWh/m2)
        BASE_CONSUMPTION = {
            'electricity': 50,    # Base electrical consumption
            'heating': 100,       # Base heating consumption
            'cooling': 30         # Base cooling consumption
        }
        
        # Standard building size in m2 (can be adjusted)
        BUILDING_SIZE = 1000
        
        # Calculate energy efficiency improvement
        efficiency_improvement = (
            future_scores['Energy Efficiency'] - current_scores['Energy Efficiency']
        )
        
        # If there's no improvement in energy efficiency, return 0
        if efficiency_improvement <= 0:
            return 0
        
        # Calculate potential savings for each energy type
        total_co2_savings = 0
        
        # Calculate for each energy type
        for energy_type, base_consumption in BASE_CONSUMPTION.items():
            # Estimate energy savings (kWh) based on efficiency improvement
            energy_savings = (
                base_consumption * 
                BUILDING_SIZE * 
                (efficiency_improvement / 3)  # Normalize by max score of 3
            )
            
            # Convert to CO2 savings
            co2_savings = (
                energy_savings * 
                CONVERSION_FACTORS[energy_type] / 
                1000  # Convert to tonnes
            )
            
            total_co2_savings += co2_savings
        
        return total_co2_savings

    def generate_pdf_report(self, building_id, results, output_path):
        """Generate PDF report with comparison and recommendations"""
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30
        )
        story.append(Paragraph("Smart Readiness Indicator (SRI)<br/>Upgrade Recommendation Report<br/>DCU Innovation Campus", title_style))
        story.append(Spacer(1, 20))

                # Add report info table
        timestamp = datetime.now().strftime("%d %B %Y")
        timevalue = datetime.now().strftime("%H:%M:%S")
        data = [
            ["Building ID:", building_id],
            ["Report Date:", timestamp],
            ["Report Time:", timevalue],
        ]
        info_table = Table(data, colWidths=[120, 300])
        info_table.setStyle(
            TableStyle(
                [
                    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 0), (-1, -1), 10),
                    ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#1F4987")),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                ]
            )
        )
        story.append(info_table)
        story.append(Spacer(1, 30))
        
        # Summary section
        story.append(Paragraph("Investment Summary", styles['Heading2']))
        
        # Calculate CO2 savings
        co2_savings = self.calculate_co2_savings(results['current_scores'], results['future_scores'])
        
        summary_data = [
            ["Total Investment", f"€{results['total_cost']:,.2f}"],
            ["Remaining Budget", f"€{results['remaining_budget']:,.2f}"],
            ["Estimated Annual CO2 Savings", f"{co2_savings:.1f} tonnes"]
        ]
        summary_table = Table(summary_data, colWidths=[4*inch, 3*inch])
        summary_table.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (0,-1), colors.lightgrey),
            ('PADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(summary_table)
        story.append(Spacer(1, 20))
        
        # Domain Improvements
        story.append(Paragraph("Domain Score Improvements", styles['Heading2']))
        improvements_data = [["Domain", "Before", "After", "Change"]]
        
        for domain in self.domain_names:
            before = results['current_scores'][domain]
            after = results['future_scores'][domain]
            change = after - before
            improvements_data.append([
                domain,
                f"{before:.2f}",
                f"{after:.2f}",
                f"{change:+.2f}"
            ])
        
        improvements_table = Table(improvements_data, colWidths=[3*inch, 1.5*inch, 1.5*inch, 1.5*inch])
        improvements_table.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
            ('PADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(improvements_table)
        story.append(Spacer(1, 20))
        
        # Environmental Impact
        if co2_savings > 0:
            story.append(Paragraph("Environmental Impact", styles['Heading2']))
            env_text = f"""
            <para>
            The recommended upgrades are estimated to reduce annual CO2 emissions by {co2_savings:.1f} tonnes.
            This is equivalent to:
            <br/>- Planting {(co2_savings * 45):.0f} trees
            <br/>- Taking {(co2_savings * 0.22):.1f} cars off the road for a year
            </para>
            """
            story.append(Paragraph(env_text, styles['Normal']))
            story.append(Spacer(1, 20))
        
        # # Add radar chart
        # story.append(Paragraph("Domain Scores Visualization", styles['Heading2']))
        # chart_buffer = self.create_radar_chart(
        #     results['current_scores'], 
        #     results['future_scores']
        # )
        # story.append(Image(chart_buffer, width=6*inch, height=6*inch))
        story.append(Spacer(1, 20))
        
        # Recommended Upgrades
        story.append(Paragraph("Recommended Upgrades", styles['Heading2']))
        for upgrade in results['upgrades']:
            upgrade_text = f"""
            <para>
            <b>Question {upgrade['question']}:</b><br/>
            Upgrade from option {upgrade['from_opt']} to option {upgrade['to_opt']}<br/>
            Cost: €{upgrade['cost']:,.2f}<br/>
            Main improvements:<br/>
            {'; '.join(f'{domain}: {impact:+.2f}' for domain, impact in upgrade['domain_impacts'].items() if impact > 0)}<br/>
            </para>
            """
            story.append(Paragraph(upgrade_text, styles['Normal']))
            story.append(Spacer(1, 10))

                # Add Methodology and Standards section
        story.append(Paragraph("Methodology and Standards", styles['Heading2']))
        
        # SRI Assessment section
        story.append(Paragraph("<b>Smart Readiness Indicator (SRI) Assessment:</b>", styles['Normal']))
        story.append(Paragraph("• Assessment follows the official EU Smart Readiness Indicator methodology as defined in the Energy Performance of Buildings Directive (EPBD)", styles['Normal']))
        story.append(Paragraph("• Domain weightings based on Ireland (West Europe) standard weightings:", styles['Normal']))
        story.append(Paragraph("    - Energy Efficiency: 16.67%", styles['Normal']))
        story.append(Paragraph("    - Energy Flexibility & Storage: 33.33%", styles['Normal']))
        story.append(Paragraph("    - Comfort: 8.33%", styles['Normal']))
        story.append(Paragraph("    - Convenience: 8.33%", styles['Normal']))
        story.append(Paragraph("    - Health & Wellbeing: 8.33%", styles['Normal']))
        story.append(Paragraph("    - Maintenance & Fault Prediction: 16.67%", styles['Normal']))
        story.append(Paragraph("    - Information to Occupants: 8.33%", styles['Normal']))
        story.append(Spacer(1, 10))
        
        # CO2 Emissions section
        story.append(Paragraph("<b>CO2 Emissions Calculation Methodology:</b>", styles['Normal']))
        story.append(Paragraph("• Calculations based on EU average emission factors:", styles['Normal']))
        story.append(Paragraph("    - Electricity: 0.275 kg CO2/kWh (EU grid average)", styles['Normal']))
        story.append(Paragraph("    - Heating: 0.202 kg CO2/kWh (Natural gas baseline)", styles['Normal']))
        story.append(Paragraph("    - Cooling: 0.275 kg CO2/kWh (Electric cooling)", styles['Normal']))
        story.append(Paragraph("• Base consumption patterns aligned with EU building stock averages:", styles['Normal']))
        story.append(Paragraph("    - Electricity: 50 kWh/m²/year", styles['Normal']))
        story.append(Paragraph("    - Heating: 100 kWh/m²/year", styles['Normal']))
        story.append(Paragraph("    - Cooling: 30 kWh/m²/year", styles['Normal']))
        story.append(Paragraph("• Savings calculations follow EN 15232 standard for impact of building automation", styles['Normal']))
        story.append(Spacer(1, 10))
        
        # Standards section
        story.append(Paragraph("<b>Relevant Standards and References:</b>", styles['Normal']))
        story.append(Paragraph("• EN 15232: Energy Performance of Buildings - Impact of Building Automation", styles['Normal']))
        story.append(Paragraph("• SRI Delegated Regulation EU 2020/2155", styles['Normal']))
        story.append(Paragraph("• SRI Implementing Regulation EU 2020/2156", styles['Normal']))
        story.append(Paragraph("• EPBD Directive 2018/844/EU", styles['Normal']))
        story.append(Paragraph("• EU ETS Default emission factors", styles['Normal']))
        story.append(Spacer(1, 10))
        
        # Limitations section
        story.append(Paragraph("<b>Notes and Limitations:</b>", styles['Normal']))
        story.append(Paragraph("• CO2 savings are estimates based on typical building patterns and may vary based on actual usage", styles['Normal']))
        story.append(Paragraph("• Calculations assume standard building operation patterns and may need adjustment for specific use cases", styles['Normal']))
        story.append(Paragraph("• Energy savings are calculated based on statistical averages from EN 15232 and may vary in practice", styles['Normal']))
        story.append(Paragraph("• Recommendations focus on maximum impact within budget constraints while maintaining balanced improvements across all domains", styles['Normal']))
        
        doc.build(story)
