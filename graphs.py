import pandas as pd
import matplotlib.pyplot as plt
import os


# =====================================================
# CREATE FOLDER
# =====================================================

if not os.path.exists("charts"):

    os.makedirs("charts")


# =====================================================
# LOAD CSV
# =====================================================

df = pd.read_csv("results.csv")


# =====================================================
# ALGORITHM GROUPS
# =====================================================

quadratic = [

    "Bubble Sort",
    "Insertion Sort",
    "Selection Sort"
]

efficient = [

    "Shell Sort",
    "Merge Sort",
    "Quick Sort",
    "Heap Sort"
]

special = [

    "Radix Sort",
    "TimSort"
]


# =====================================================
# CASES
# =====================================================

cases = [

    "Random",
    "Sorted",
    "Reversed",
    "Nearly Sorted"
]


# =====================================================
# CHARTS - ALGORITMI DE COMPLEXITATE PATRATICA   
# =====================================================

for case in cases:

    plt.figure(figsize=(11, 7))

    case_data = df[

        (df["Case"] == case) &
        (df["Algorithm"].isin(quadratic))
    ]

    for algo in quadratic:

        algo_data = case_data[
            case_data["Algorithm"] == algo
        ]

        plt.plot(

            algo_data["Input Size"],
            algo_data["Execution Time"],

            marker="o",
            linewidth=2.5,
            markersize=7,

            label=algo
        )

    plt.xlabel("Input Size", fontsize=13)

    plt.ylabel(
        "Execution Time (seconds)",
        fontsize=13
    )

    plt.title(
        f"Algoritmi de complexitate patratica - {case}",
        fontsize=18
    )

    plt.grid(True, alpha=0.3)

    plt.legend(fontsize=11)

    plt.tight_layout()

    plt.savefig(
        f"charts/quadratic_{case}.png",
        dpi=300
    )

    plt.close()


# =====================================================
# CHARTS - ALGORITMI EFICIENTI
# =====================================================

for case in cases:

    plt.figure(figsize=(11, 7))

    case_data = df[

        (df["Case"] == case) &
        (df["Algorithm"].isin(efficient))
    ]

    for algo in efficient:

        algo_data = case_data[
            case_data["Algorithm"] == algo
        ]

        plt.plot(

            algo_data["Input Size"],
            algo_data["Execution Time"],

            marker="o",
            linewidth=2.5,
            markersize=7,

            label=algo
        )

    plt.xlabel("Input Size", fontsize=13)

    plt.ylabel(
        "Execution Time (seconds)",
        fontsize=13
    )

    plt.title(
        f"Algoritmi eficienti - {case}",
        fontsize=18
    )

    plt.grid(True, alpha=0.3)

    plt.legend(fontsize=11)

    plt.tight_layout()

    plt.savefig(
        f"charts/efficient_{case}.png",
        dpi=300
    )

    plt.close()


# =====================================================
# CHARTS - ALGORITMI SPECIALIZATI
# =====================================================

for case in cases:

    plt.figure(figsize=(11, 7))

    case_data = df[

        (df["Case"] == case) &
        (df["Algorithm"].isin(special))
    ]

    for algo in special:

        algo_data = case_data[
            case_data["Algorithm"] == algo
        ]

        plt.plot(

            algo_data["Input Size"],
            algo_data["Execution Time"],

            marker="o",
            linewidth=2.5,
            markersize=7,

            label=algo
        )

    plt.xlabel("Input Size", fontsize=13)

    plt.ylabel(
        "Execution Time (seconds)",
        fontsize=13
    )

    plt.title(
        f"Algoritmi specializati - {case}",
        fontsize=18
    )

    plt.grid(True, alpha=0.3)

    plt.legend(fontsize=11)

    plt.tight_layout()

    plt.savefig(
        f"charts/special_{case}.png",
        dpi=300
    )

    plt.close()


# =====================================================
# BAR CHART (LOG SCALE)
# =====================================================

largest_size = df["Input Size"].max()

largest_df = df[
    df["Input Size"] == largest_size
]

avg_times = largest_df.groupby(
    "Algorithm"
)["Execution Time"].mean()

avg_times = avg_times.sort_values()

plt.figure(figsize=(13, 7))

plt.bar(
    avg_times.index,
    avg_times.values
)

plt.yscale("log")

plt.title(
    f"Average Performance at {largest_size} Elements (Log Scale)",
    fontsize=18
)

plt.xlabel("Algorithm", fontsize=13)

plt.ylabel(
    "Average Execution Time (seconds - log scale)",
    fontsize=13
)

plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "charts/bar_chart_log.png",
    dpi=300
)

plt.close()


# =====================================================
# SCALABILITY CHART
# =====================================================

plt.figure(figsize=(13, 8))

algorithms = df["Algorithm"].unique()

for algo in algorithms:

    algo_data = df[
        df["Algorithm"] == algo
    ]

    grouped = algo_data.groupby(
        "Input Size"
    )["Execution Time"].mean()

    plt.plot(

        grouped.index,
        grouped.values,

        marker="o",
        linewidth=2.5,

        label=algo
    )

plt.xlabel("Input Size", fontsize=13)

plt.ylabel(
    "Average Execution Time",
    fontsize=13
)

plt.title(
    "Algorithm Scalability",
    fontsize=18
)

plt.grid(True, alpha=0.3)

plt.legend()

plt.tight_layout()

plt.savefig(
    "charts/scalability_chart.png",
    dpi=300
)

plt.close()


# =====================================================
# RANKING TABLE
# =====================================================

ranking = df.groupby(
    "Algorithm"
)["Execution Time"].mean()

ranking = ranking.sort_values()

ranking.to_csv(
    "charts/ranking_table.csv"
)


# =====================================================
# COMPLEXITY TABLE
# =====================================================

complexity = pd.DataFrame({

    "Algorithm": [

        "Bubble Sort",
        "Insertion Sort",
        "Selection Sort",

        "Shell Sort",
        "Merge Sort",
        "Quick Sort",
        "Heap Sort",

        "Radix Sort",
        "TimSort"
    ],

    "Best Case": [

        "O(n)",
        "O(n)",
        "O(n²)",

        "O(n log n)",
        "O(n log n)",
        "O(n log n)",
        "O(n log n)",

        "O(nk)",
        "O(n)"
    ],

    "Average Case": [

        "O(n²)",
        "O(n²)",
        "O(n²)",

        "O(n log² n)",
        "O(n log n)",
        "O(n log n)",
        "O(n log n)",

        "O(nk)",
        "O(n log n)"
    ],

    "Worst Case": [

        "O(n²)",
        "O(n²)",
        "O(n²)",

        "O(n²)",
        "O(n log n)",
        "O(n²)",
        "O(n log n)",

        "O(nk)",
        "O(n log n)"
    ]
})

complexity.to_csv(

    "charts/complexity_table.csv",

    index=False
)

print("\nAll charts generated successfully!")