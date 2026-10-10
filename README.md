# Jar Growth Intern Assignment

This repository contains my completed Jar Growth Intern assignment. It includes:

- **Q1 - Sales Analysis:** Python-based analysis of sales, profitability, target achievement, and regional performance using the supplied order, order-detail, and sales-target datasets.
- **Q2 - Jar App Analysis:** Product and growth analysis of Jar's app experience, strengths, user-facing improvement opportunities, and business implications.
- **Q3 - New Business Opportunities:** Evaluation of five potential growth opportunities for Jar, with prioritization, assumptions, risks, and a 30-60-90 day test plan.

The Q1 work is implemented with scripts, notebooks, processed datasets, tables, and charts. Q2 and Q3 are submitted as PDF reports.

## Repository Structure

```text
.
|-- Q1_Sales_Analysis/
|   |-- Part_1_Sales_Profitability/
|   |   |-- data/
|   |   |   |-- raw/
|   |   |   |   |-- List_of_Orders_-_List_of_Orders.pdf
|   |   |   |   `-- Order_Details_-_Order_Details.pdf
|   |   |   `-- processed/
|   |   |       |-- list_of_orders.csv
|   |   |       |-- order_details.csv
|   |   |       `-- merged_order_data.csv
|   |   |-- notebooks/
|   |   |   `-- sales_profitability_analysis.ipynb
|   |   |-- outputs/
|   |   |   |-- charts/
|   |   |   |   |-- profit_margin_by_category.png
|   |   |   |   `-- total_sales_by_category.png
|   |   |   `-- tables/
|   |   |       |-- category_analysis_findings.md
|   |   |       `-- category_performance_summary.csv
|   |   `-- scripts/
|   |       |-- category_analysis.py
|   |       |-- create_charts.py
|   |       |-- extract_data.py
|   |       `-- merge_data.py
|   |-- Part_2_Target_Achievement/
|   |   |-- data/
|   |   |   |-- raw/
|   |   |   |   `-- Sales_target_-_Sales_target.pdf
|   |   |   `-- processed/
|   |   |       |-- sales_target.csv
|   |   |       `-- sales_target_clean.csv
|   |   |-- notebooks/
|   |   |   `-- target_achievement_analysis.ipynb
|   |   |-- outputs/
|   |   |   |-- charts/
|   |   |   |   |-- furniture_mom_target_change.png
|   |   |   |   |-- furniture_target_achievement.png
|   |   |   |   `-- furniture_target_vs_actual.png
|   |   |   `-- tables/
|   |   |       `-- furniture_target_analysis.csv
|   |   `-- scripts/
|   |       |-- create_charts.py
|   |       `-- target_analysis.py
|   `-- Part_3_Regional_Performance/
|       |-- data/
|       |   |-- raw/
|       |   |   `-- List_of_Orders_-_List_of_Orders.pdf
|       |   `-- processed/
|       |       `-- list_of_orders.csv
|       |-- notebooks/
|       |   `-- regional_performance_analysis.ipynb
|       |-- outputs/
|       |   |-- charts/
|       |   |   |-- average_profit_by_top_5_states.png
|       |   |   |-- city_profitability_top_5_states.png
|       |   |   `-- orders_by_top_5_states.png
|       |   `-- tables/
|       |       |-- regional_improvement_candidates.csv
|       |       |-- top_5_states_analysis.csv
|       |       `-- top_5_states_city_analysis.csv
|       `-- scripts/
|           |-- create_charts.py
|           `-- regional_analysis.py
|-- Q2/
|   `-- Jar_Growth_Intern_Q2.pdf
|-- Q3/
|   `-- Jar_Growth_Intern_Q3.pdf
`-- README.md
```

## Q1 - Sales Analysis

Q1 analyzes the supplied sales datasets across three parts. The analysis uses the List of Orders, Order Details, and Sales Target data, with outputs saved as CSV tables and PNG charts.

### Part 1: Sales and Profitability

Part 1 merges the List of Orders and Order Details datasets on `Order ID`, using a one-to-many relationship because each order can contain multiple product lines. The analysis calculates category-level total sales, total profit, average profit per order containing that category, and profit margin.

Average profit per order means average profit per order containing that category. It is calculated by first grouping by `Order ID` + `Category`, summing profit at that level, and then averaging those order-category totals by category. Profit margin is calculated from category totals as:

```text
Total Profit / Total Sales * 100
```

Key findings:

- Electronics has the highest total sales at Rs 165,267 and the highest average profit per order containing that category at Rs 51.44.
- Clothing has the highest total profit at Rs 11,163 and the highest profit margin at 8.03%.
- Furniture is the weakest category by profitability, with Rs 2,298 total profit, Rs 12.35 average profit per order containing that category, and a 1.81% margin.
- Tables and Electronic Games are loss-making sub-categories and should be investigated for pricing, discounting, or cost issues.
- Sarees generate high sales but only a 0.66% margin, making them an important low-margin segment to review.

Relevant files:

- Notebook: [Q1_Sales_Analysis/Part_1_Sales_Profitability/notebooks/sales_profitability_analysis.ipynb](Q1_Sales_Analysis/Part_1_Sales_Profitability/notebooks/sales_profitability_analysis.ipynb)
- Scripts: [extract_data.py](Q1_Sales_Analysis/Part_1_Sales_Profitability/scripts/extract_data.py), [merge_data.py](Q1_Sales_Analysis/Part_1_Sales_Profitability/scripts/merge_data.py), [category_analysis.py](Q1_Sales_Analysis/Part_1_Sales_Profitability/scripts/category_analysis.py), [create_charts.py](Q1_Sales_Analysis/Part_1_Sales_Profitability/scripts/create_charts.py)
- Output table: [category_performance_summary.csv](Q1_Sales_Analysis/Part_1_Sales_Profitability/outputs/tables/category_performance_summary.csv)
- Written findings: [category_analysis_findings.md](Q1_Sales_Analysis/Part_1_Sales_Profitability/outputs/tables/category_analysis_findings.md)
- Charts: [total_sales_by_category.png](Q1_Sales_Analysis/Part_1_Sales_Profitability/outputs/charts/total_sales_by_category.png), [profit_margin_by_category.png](Q1_Sales_Analysis/Part_1_Sales_Profitability/outputs/charts/profit_margin_by_category.png)

### Part 2: Target Achievement

Part 2 analyzes Furniture sales targets from the Sales Target dataset. Furniture target records are converted to month values, sorted chronologically, and then used to calculate month-over-month percentage change.

The month-over-month target change formula is:

```text
(Current Month Target - Previous Month Target) / Previous Month Target * 100
```

An absolute month-over-month target change greater than 1.5% is flagged as a relatively significant fluctuation. This threshold is an analytical convention used to highlight larger changes within this dataset; it is not provided by the source data.

Key findings:

- Furniture targets increase consistently from April 2018 through March 2019.
- The largest target increases occur in July 2018 (+1.89%), November 2018 (+1.80%), and March 2019 (+1.72%).
- Actual Furniture sales are more volatile than the target trajectory.
- Actual sales substantially underperform the target during several early and middle months, while November 2018 and January-March 2019 exceed target.
- Target-setting could benefit from incorporating recent actual performance and demand variability rather than relying only on a steady month-over-month increase.

Relevant files:

- Notebook: [Q1_Sales_Analysis/Part_2_Target_Achievement/notebooks/target_achievement_analysis.ipynb](Q1_Sales_Analysis/Part_2_Target_Achievement/notebooks/target_achievement_analysis.ipynb)
- Scripts: [target_analysis.py](Q1_Sales_Analysis/Part_2_Target_Achievement/scripts/target_analysis.py), [create_charts.py](Q1_Sales_Analysis/Part_2_Target_Achievement/scripts/create_charts.py)
- Output table: [furniture_target_analysis.csv](Q1_Sales_Analysis/Part_2_Target_Achievement/outputs/tables/furniture_target_analysis.csv)
- Charts: [furniture_target_vs_actual.png](Q1_Sales_Analysis/Part_2_Target_Achievement/outputs/charts/furniture_target_vs_actual.png), [furniture_target_achievement.png](Q1_Sales_Analysis/Part_2_Target_Achievement/outputs/charts/furniture_target_achievement.png), [furniture_mom_target_change.png](Q1_Sales_Analysis/Part_2_Target_Achievement/outputs/charts/furniture_mom_target_change.png)

### Part 3: Regional Performance

Part 3 identifies the five states with the highest order count using the List of Orders dataset. Sales and profit are first aggregated to one record per `Order ID` from the merged order-detail data, then joined back to List of Orders for regional analysis. This prevents orders with multiple line items from receiving disproportionate weight.

Top five states by order count:

| State | Order Count | Total Sales | Average Profit / Order |
|---|---:|---:|---:|
| Madhya Pradesh | 101 | Rs 105,140 | Rs 54.96 |
| Maharashtra | 90 | Rs 95,348 | Rs 68.62 |
| Rajasthan | 32 | Rs 21,149 | Rs 39.28 |
| Gujarat | 27 | Rs 21,058 | Rs 17.22 |
| Punjab | 25 | Rs 16,786 | -Rs 24.36 |

Regional findings:

- Madhya Pradesh has the highest order volume and total sales among the top five states.
- Maharashtra has fewer orders than Madhya Pradesh but higher average profit per order.
- Punjab has negative average profit per order and is the clearest state-level profitability concern among the top five.
- Chandigarh, Ahmedabad, and Jaipur are city-level profitability investigation candidates because their average profit per order is negative.
- Mumbai is not loss-making in the dataset, but its high order volume and comparatively low average profit suggest an optimization opportunity.

Data-quality caveat: the dataset contains 3 records where Delhi appears as the city under Madhya Pradesh. The supplied dataset and reported results are left unchanged; this should be treated as a data-quality inconsistency rather than used as a regional business conclusion.

Relevant files:

- Notebook: [Q1_Sales_Analysis/Part_3_Regional_Performance/notebooks/regional_performance_analysis.ipynb](Q1_Sales_Analysis/Part_3_Regional_Performance/notebooks/regional_performance_analysis.ipynb)
- Scripts: [regional_analysis.py](Q1_Sales_Analysis/Part_3_Regional_Performance/scripts/regional_analysis.py), [create_charts.py](Q1_Sales_Analysis/Part_3_Regional_Performance/scripts/create_charts.py)
- Output tables: [top_5_states_analysis.csv](Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/tables/top_5_states_analysis.csv), [top_5_states_city_analysis.csv](Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/tables/top_5_states_city_analysis.csv), [regional_improvement_candidates.csv](Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/tables/regional_improvement_candidates.csv)
- Charts: [orders_by_top_5_states.png](Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/charts/orders_by_top_5_states.png), [average_profit_by_top_5_states.png](Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/charts/average_profit_by_top_5_states.png), [city_profitability_top_5_states.png](Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/charts/city_profitability_top_5_states.png)

## Q2 - Jar App Analysis

Q2 is a product and growth analysis of Jar's app experience. The report reviews Jar's public app journeys, website, app-store listings, available company and press information, and a small sample of public user reviews. It distinguishes sourced facts, observations, interpretations, hypotheses, and illustrative estimates.

The analysis covers Jar's core product context: 24K digital gold savings, UPI AutoPay, instant saving, rewards, withdrawal, jewellery through Nek, and availability-dependent services listed publicly such as loans, health insurance, and UPI payments.

Strengths identified in the report:

- Low entry point and flexible savings rhythm, including small daily, weekly, monthly, and instant-saving options.
- UPI AutoPay as a retention mechanism because it removes the daily decision to save.
- Minimal-step, multilingual onboarding that can reduce friction for first-time formal savers.
- A bridge from digital gold to physical gold or jewellery through Nek.
- Visible trust and anti-fraud signals, including named custody, trustee, insurance, reconciliation, and fraud-warning references from Jar's public materials.

Improvement opportunities:

- Show the true cost of exit before purchase and withdrawal, including GST and spread implications.
- Add a plain-language card explaining how gold is held and what is not regulated.
- Make withdrawal availability and timing explicit.
- Build AutoPay controls for irregular-income users, such as pause or skip options where feasible.
- Add a trackable support process for common money-movement issues.

Business-growth implications are framed as testable hypotheses: clearer costs and risks may reduce regret-driven exits; predictable withdrawals and better AutoPay controls may improve retention; better support may reduce cost to serve; and jewellery cross-sell should be measured by contribution per active saver rather than gross purchase value. Public reviews are treated as anecdotal evidence, not representative Jar company data.

Deliverable: [Q2/Jar_Growth_Intern_Q2.pdf](Q2/Jar_Growth_Intern_Q2.pdf)

## Q3 - New Business Opportunities

Q3 evaluates five possible business opportunities for Jar using filters such as reuse of existing infrastructure, revenue and engagement potential, retention impact, fit with Jar's current assets, complexity, trust risk, and regulatory exposure. All scenario numbers in the PDF are illustrative assumptions, not verified Jar operating metrics.

The five opportunities are:

1. **Nek Gold Goals:** Goal-based jewellery savings that connect recurring gold saving with a specific jewellery target on Nek.
2. **Gold Gifting for occasions:** A gifting flow where a saver sends digital gold for occasions, and the recipient may become a new saver.
3. **Jar Protect:** Savings-triggered insurance and renewals, subject to distribution status, legal review, and regulatory constraints.
4. **Regulated Gold Ladder:** A partner-led route into a SEBI-regulated gold SIP or fund structure for users ready to move beyond digital gold.
5. **Jar Gold Tech for partners:** B2B embedded gold savings infrastructure for partners such as payment apps, NBFCs, neobanks, or gig-platform payout apps.

Recommended top two:

- **#1 Nek Gold Goals:** Recommended for testing first because it reuses Jar's existing recurring saving, AutoPay, gold balance, and Nek commerce path. It tests whether a concrete goal improves saving behavior, goal completion, Nek redemption, contribution margin, and 90-day retention.
- **#2 Gold Gifting for occasions:** Recommended second because it reuses similar rails and can test whether gift recipients become active savers. The report frames this as an acquisition-quality test, not mainly a direct-revenue bet.

The other three opportunities are held back because they require additional validation. Jar Protect depends on insurance distribution status and commission rules. Regulated Gold Ladder needs a legally clean partner-led structure. Jar Gold Tech could be large but depends on regulatory clarity, partner appetite, and operational feasibility.

Important assumptions and risks:

- Digital gold regulatory treatment is uncertain; SEBI has stated that digital gold is outside its framework, and the Q3 report discusses unresolved BUDS Act-related proceedings and possible future rules.
- Active users, Nek margins, and gold revenue per active saver are not public.
- Store-review evidence is qualitative and not representative.
- Behavioural assumptions, such as goal tags improving AutoPay continuity or gifts converting recipients into savers, need controlled tests.
- Cannibalisation and margin pressure should be measured before scaling.
- Any goal-like, gift-like, insurance, regulated investment, or partner product should receive legal and compliance review before launch.

Deliverable: [Q3/Jar_Growth_Intern_Q3.pdf](Q3/Jar_Growth_Intern_Q3.pdf)

## Key Findings and Recommendations

### Q1 Data Findings

- Category performance differs by metric: Electronics leads sales, Clothing leads total profit and margin, and Furniture underperforms on profitability.
- The Furniture target path rises steadily, but actual Furniture sales are much more volatile.
- Regional performance is uneven: Madhya Pradesh leads order count and sales among the top five states, Maharashtra has stronger average profit per order, and Punjab shows negative average profit.
- Chandigarh, Ahmedabad, Jaipur, Tables, Electronic Games, and Sarees are practical investigation areas based on the available data.
- The Delhi/Madhya Pradesh city-state inconsistency is a data-quality caveat and should not be used as a business conclusion.

### Q2 Product Observations

- Jar's strongest product advantages appear to be low-friction saving, UPI AutoPay, accessible onboarding, jewellery linkage, and trust signaling.
- The most important improvement areas relate to trust and expectations: exit cost visibility, regulatory/custody clarity, withdrawal timing, AutoPay control, and support transparency.
- Public app-store reviews are anecdotal, so they should guide investigation rather than be treated as representative user research.

### Q3 Proposed Opportunities

- Nek Gold Goals and Gold Gifting are the top recommended tests because they reuse existing Jar assets and can be validated quickly.
- Jar Protect, Regulated Gold Ladder, and Jar Gold Tech should wait for legal, regulatory, economic, or partner-demand validation.
- All Q3 revenue figures are illustrative scenarios and should be replaced with Jar's internal data before investment decisions.

## Tools, Methodology, and Reproducibility

The Q1 analysis is implemented in Python with pandas and matplotlib. The existing local virtual environment is located under:

```text
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/
```

No repository-level dependency file is present. The commands below use the existing local virtual environment and should be run from the repository root:

```bash
# Q1 Part 1: extract raw PDFs to CSV, merge orders, analyze categories, and create charts
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/bin/python Q1_Sales_Analysis/Part_1_Sales_Profitability/scripts/extract_data.py
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/bin/python Q1_Sales_Analysis/Part_1_Sales_Profitability/scripts/merge_data.py
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/bin/python Q1_Sales_Analysis/Part_1_Sales_Profitability/scripts/category_analysis.py
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/bin/python Q1_Sales_Analysis/Part_1_Sales_Profitability/scripts/create_charts.py

# Q1 Part 2: analyze Furniture target achievement and create charts
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/bin/python Q1_Sales_Analysis/Part_2_Target_Achievement/scripts/target_analysis.py
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/bin/python Q1_Sales_Analysis/Part_2_Target_Achievement/scripts/create_charts.py

# Q1 Part 3: analyze regional performance and create charts
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/bin/python Q1_Sales_Analysis/Part_3_Regional_Performance/scripts/regional_analysis.py
Q1_Sales_Analysis/Part_1_Sales_Profitability/.venv/bin/python Q1_Sales_Analysis/Part_3_Regional_Performance/scripts/create_charts.py
```

Generated Q1 outputs are stored in each part's `outputs/tables/` and `outputs/charts/` directories. The notebooks in each part provide the narrative analysis and visual review.

## Deliverables

- Q1 Part 1 notebook: [Q1_Sales_Analysis/Part_1_Sales_Profitability/notebooks/sales_profitability_analysis.ipynb](Q1_Sales_Analysis/Part_1_Sales_Profitability/notebooks/sales_profitability_analysis.ipynb)
- Q1 Part 1 category summary: [Q1_Sales_Analysis/Part_1_Sales_Profitability/outputs/tables/category_performance_summary.csv](Q1_Sales_Analysis/Part_1_Sales_Profitability/outputs/tables/category_performance_summary.csv)
- Q1 Part 1 written findings: [Q1_Sales_Analysis/Part_1_Sales_Profitability/outputs/tables/category_analysis_findings.md](Q1_Sales_Analysis/Part_1_Sales_Profitability/outputs/tables/category_analysis_findings.md)
- Q1 Part 2 notebook: [Q1_Sales_Analysis/Part_2_Target_Achievement/notebooks/target_achievement_analysis.ipynb](Q1_Sales_Analysis/Part_2_Target_Achievement/notebooks/target_achievement_analysis.ipynb)
- Q1 Part 2 target table: [Q1_Sales_Analysis/Part_2_Target_Achievement/outputs/tables/furniture_target_analysis.csv](Q1_Sales_Analysis/Part_2_Target_Achievement/outputs/tables/furniture_target_analysis.csv)
- Q1 Part 3 notebook: [Q1_Sales_Analysis/Part_3_Regional_Performance/notebooks/regional_performance_analysis.ipynb](Q1_Sales_Analysis/Part_3_Regional_Performance/notebooks/regional_performance_analysis.ipynb)
- Q1 Part 3 state table: [Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/tables/top_5_states_analysis.csv](Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/tables/top_5_states_analysis.csv)
- Q1 Part 3 city table: [Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/tables/top_5_states_city_analysis.csv](Q1_Sales_Analysis/Part_3_Regional_Performance/outputs/tables/top_5_states_city_analysis.csv)
- Q2 PDF report: [Q2/Jar_Growth_Intern_Q2.pdf](Q2/Jar_Growth_Intern_Q2.pdf)
- Q3 PDF report: [Q3/Jar_Growth_Intern_Q3.pdf](Q3/Jar_Growth_Intern_Q3.pdf)
