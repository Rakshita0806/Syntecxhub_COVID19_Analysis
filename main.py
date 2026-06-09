import pandas as pd
import matplotlib.pyplot as plt
import os


os.makedirs("outputs", exist_ok=True)


df = pd.read_csv("data/covid_data.csv")


df["date"] = pd.to_datetime(df["date"])


countries = ["India", "United States", "Brazil"]
df = df[df["location"].isin(countries)]


df = df[["location", "date", "new_cases", "total_cases"]]


df = df.dropna(subset=["new_cases"])

print("=" * 50)
print("COVID-19 DATA ANALYSIS")
print("=" * 50)


plt.figure(figsize=(12, 6))

for country in countries:
    country_df = df[df["location"] == country]

    plt.plot(
        country_df["date"],
        country_df["new_cases"],
        label=country
    )

plt.title("Daily COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/daily_cases.png")
plt.close()

print("Saved: daily_cases.png")

plt.figure(figsize=(12, 6))

for country in countries:
    country_df = df[df["location"] == country].copy()

    country_df["rolling_avg"] = (
        country_df["new_cases"]
        .rolling(window=7)
        .mean()
    )

    plt.plot(
        country_df["date"],
        country_df["rolling_avg"],
        label=country
    )

plt.title("7-Day Rolling Average of COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("Rolling Average Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/rolling_average.png")
plt.close()

print("Saved: rolling_average.png")


plt.figure(figsize=(12, 6))

for country in countries:
    country_df = df[df["location"] == country]

    plt.plot(
        country_df["date"],
        country_df["total_cases"],
        label=country
    )

plt.title("Total COVID-19 Cases Comparison")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/country_comparison.png")
plt.close()

print("Saved: country_comparison.png")


peak_data = []

for country in countries:
    country_df = df[df["location"] == country]

    peak_cases = country_df["new_cases"].max()

    peak_row = country_df.loc[
        country_df["new_cases"].idxmax()
    ]

    peak_date = peak_row["date"]

    peak_data.append(
        {
            "Country": country,
            "Peak Cases": peak_cases,
            "Peak Date": peak_date
        }
    )

peak_df = pd.DataFrame(peak_data)

plt.figure(figsize=(8, 5))

plt.bar(
    peak_df["Country"],
    peak_df["Peak Cases"]
)

plt.title("Peak Daily Cases by Country")
plt.xlabel("Country")
plt.ylabel("Peak Daily Cases")

plt.tight_layout()

plt.savefig("outputs/peaks.png")
plt.close()

print("Saved: peaks.png")


print("\nPEAK ANALYSIS")
print("-" * 50)

for _, row in peak_df.iterrows():
    print(
        f"{row['Country']} -> "
        f"{int(row['Peak Cases'])} cases "
        f"on {row['Peak Date'].date()}"
    )

highest_peak = peak_df.loc[
    peak_df["Peak Cases"].idxmax()
]

print("\nSUMMARY")
print("-" * 50)

print(
    f"Highest peak recorded by "
    f"{highest_peak['Country']} "
    f"with {int(highest_peak['Peak Cases'])} cases."
)

print("\nAll charts saved successfully in outputs folder.")