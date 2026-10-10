# Q1 Part 3 — Regional Performance Insights

## Objective

Identify the top 5 states by order count from the List of Orders dataset, calculate total sales and average profit for those states, highlight regional disparities, and identify regions or cities that should be prioritized for improvement.

## Data Sources

- List of Orders dataset
- Order Details dataset reused from Q1 Part 1 for order-level sales and profit calculations

## Methodology

1. Start with the List of Orders dataset containing one record per order.
2. Aggregate Order Details at the Order ID level to calculate:
   - Total Sales per Order
   - Total Profit per Order
3. Merge these order-level metrics with the List of Orders dataset.
4. Calculate state-level:
   - Unique Order Count
   - Total Sales
   - Average Profit per Order
5. Rank states by order count and select the top 5.
6. Analyze cities within these top 5 states to identify concentrated profitability issues.

Average profit is calculated at the order level first and then averaged by state/city so that orders containing multiple product line items do not receive disproportionate weight.

## Key Findings

| State | Order Count | Total Sales | Average Profit / Order |
|---|---:|---:|---:|
| Madhya Pradesh | 101 | ₹105,140 | ₹54.96 |
| Maharashtra | 90 | ₹95,348 | ₹68.62 |
| Rajasthan | 32 | ₹21,149 | ₹39.28 |
| Gujarat | 27 | ₹21,058 | ₹17.22 |
| Punjab | 25 | ₹16,786 | -₹24.36 |

### Regional Disparities

- Madhya Pradesh has the highest order volume and total sales among the top 5 states.
- Maharashtra has fewer orders than Madhya Pradesh but a higher average profit per order.
- Punjab has negative average profit per order and requires profitability-focused investigation.
- Gujarat has relatively low average profitability despite generating more than ₹21K in sales.
- Rajasthan shows moderate scale but has a significant city-level profitability difference.

### City-Level Priorities

- Chandigarh: -₹72.06 average profit/order
- Ahmedabad: -₹51.76 average profit/order
- Jaipur: -₹39.63 average profit/order
- Mumbai: ₹24.07 average profit/order despite the highest order volume within Maharashtra

These cities should be investigated for factors such as product mix, pricing, discounting, and other operational or cost-related drivers. The available dataset does not contain enough information to establish the exact cause of the negative profitability.

## Recommendations

1. Prioritize Chandigarh for profitability improvement because it combines negative average profit with relatively high order volume.
2. Investigate Ahmedabad and Jaipur for city-specific profitability issues.
3. Review Mumbai's product mix and profitability because of its high order volume but comparatively low average profit.
4. Use Madhya Pradesh and Pune as examples of regions/cities with positive performance that may provide useful benchmarks.
5. Before changing regional targets or strategies, investigate pricing, discounting, product mix, and operational factors using additional business data.

## Data Quality Note

The dataset contains 3 records where Delhi appears as the city under Madhya Pradesh. This should be treated as a data-quality inconsistency rather than used as a regional business conclusion.
