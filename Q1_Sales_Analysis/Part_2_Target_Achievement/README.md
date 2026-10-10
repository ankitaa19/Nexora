# Part 2 — Target Achievement Analysis

## Objective

Analyze monthly target sales for the Furniture category, calculate month-over-month target changes, compare targets with actual Furniture sales, identify significant fluctuations, and suggest strategies for improving target alignment.

## Data Sources

### Sales Target Dataset
Original source:
`data/raw/Sales_target_-_Sales_target.pdf`

The PDF contains monthly sales targets for Furniture, Clothing, and Electronics.

### Actual Sales Dataset
Actual Furniture sales are derived from the processed dataset created in Part 1:

`../Part_1_Sales_Profitability/data/processed/merged_order_data.csv`

The Part 2 analysis reuses this processed dataset rather than duplicating the original order PDFs.

## Analysis

The analysis includes:

- Furniture month-over-month target change
- Monthly actual Furniture sales
- Target achievement percentage
- Target vs actual sales gap
- Identification of relatively large target fluctuations
- Business interpretation of target and actual performance
- Strategies for improving target-setting alignment

## Significant Target Fluctuation

For analytical purposes, an absolute month-over-month target change greater than 1.5% is flagged as a relatively significant fluctuation.

This threshold is an analytical convention used to highlight larger changes within this dataset; it is not a threshold provided by the source data.

## Key Findings

Furniture targets increase consistently from April 2018 through March 2019, while actual Furniture sales show substantially greater month-to-month variability.

The largest target increases occur in:

- July 2018 — 1.89%
- November 2018 — 1.80%
- March 2019 — 1.72%

Actual Furniture sales substantially underperform the target during several early and middle months, while November 2018 and January–March 2019 exceed the target.

The analysis therefore suggests that target-setting could benefit from incorporating recent actual performance and demand variability rather than relying only on a steady month-over-month increase.

## Outputs

### Tables

`outputs/tables/furniture_target_analysis.csv`

### Charts

- `outputs/charts/furniture_target_vs_actual.png`
- `outputs/charts/furniture_target_achievement.png`
- `outputs/charts/furniture_mom_target_change.png`

## Scripts

- `scripts/target_analysis.py` — calculates target changes and target-vs-actual metrics
- `scripts/create_charts.py` — generates analysis charts
