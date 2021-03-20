import matplotlib.pyplot as plt
import numpy as np

starting_rank = 2500
ending_rank = 4200
no_of_plots = 5
expected_students_lower = 550_000
expected_students_upper = 610_000


def f(x, rank):
    return (x-rank)/x*100


def main():
    x = np.arange(expected_students_lower, expected_students_upper, 1)

    for rank in np.linspace(starting_rank, ending_rank, no_of_plots):
        plt.plot(x, f(x, round(rank)), label=f"{rank}")

    plt.title("JEE Percentile")
    plt.legend()
    plt.xlabel("Expected candidates")
    plt.ylabel("Percentile %")

    plt.show()


if __name__ == "__main__":
    main()
