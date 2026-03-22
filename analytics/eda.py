import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, encoding="latin1")
    return df

def basic_eda(df):
    summary = df.describe(include="all").to_string()
    nulls = df.isnull().sum().to_string()
    
    return {
        "summary": summary,
        "nulls": nulls
    }

def generate_insights(df):
    insights = []

    # Example: Sales insights
    if "Sales" in df.columns:
        total_sales = df["Sales"].sum()
        insights.append(f"Total Sales: {total_sales}")

    # Profit insights
    if "Profit" in df.columns:
        avg_profit = df["Profit"].mean()
        insights.append(f"Average Profit: {avg_profit}")

    # Top category
    if "Category" in df.columns:
        top_category = df.groupby("Category")["Sales"].sum().idxmax()
        insights.append(f"Top performing category: {top_category}")

    # Region analysis
    if "Region" in df.columns:
        worst_region = df.groupby("Region")["Profit"].sum().idxmin()
        insights.append(f"Worst performing region: {worst_region}")

    return "\n".join(insights)

def format_for_llm(eda, insights):
    return f"""
You are a business analyst.

Here is the dataset analysis:

SUMMARY:
{eda['summary']}

MISSING VALUES:
{eda['nulls']}

INSIGHTS:
{insights}

Based on this, answer user questions and suggest improvements.
"""

def analyze_data(file_path):
    df = load_data(file_path)
    eda = basic_eda(df)
    insights = generate_insights(df)
    formatted = format_for_llm(eda, insights)

    return formatted

if __name__ == "__main__":
    result = analyze_data("data/Sample - Superstore.csv")
    print(result)