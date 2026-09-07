public class bigO {
	public static void main(String[] args) {
		int[] numbers = { 4, 8, 15, 16, 23, 42 };

		System.out.println("O(1): " + firstElement(numbers));
		System.out.println("O(n): " + sum(numbers));
		printPairs(numbers);
		binarySearch(numbers, 23);
	}

	// O(1): one operation, regardless of array size.
	public static int firstElement(int[] numbers) {
		return numbers[0];
	}

	// O(n): visits every element once.
	public static int sum(int[] numbers) {
		int total = 0;
		for (int number : numbers) {
			total += number;
		}
		return total;
	}

	// O(n^2): two nested loops.
	public static void printPairs(int[] numbers) {
		System.out.println("O(n^2): pairs");
		for (int first : numbers) {
			for (int second : numbers) {
				System.out.println(first + ", " + second);
			}
		}
	}

	// O(log n): halves the search range each step.
	public static void binarySearch(int[] numbers, int target) {
		int low = 0;
		int high = numbers.length - 1;

		while (low <= high) {
			int middle = low + (high - low) / 2;
			if (numbers[middle] == target) {
				System.out.println("O(log n): found " + target);
				return;
			}
			if (numbers[middle] < target) {
				low = middle + 1;
			} else {
				high = middle - 1;
			}
		}

		System.out.println("O(log n): " + target + " was not found");
	}
}
