import matplotlib.pyplot as plt
import numpy as np


def percentile(x, rank):
    return (x-rank)/x*100


def main():
    x = np.arange(expected_students_lower, expected_students_upper, 1)

    for rank in np.linspace(starting_rank, ending_rank, no_of_plots):
        plt.plot(x, percentile(x, round(rank)), label=f"{round(rank)}")

    plt.title("JEE Percentile")
    plt.legend()
    plt.xlabel("Expected candidates")
    plt.ylabel("Percentile %")

    plt.show()


if __name__ == "__main__":
    main()
