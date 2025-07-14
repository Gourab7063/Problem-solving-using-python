def process_test_case():
    try:
        x = int(input())
        y_str = input().split()

        def calculate_sum(index, current_sum):
            if index == x:
                return str(current_sum)
            try:
                val = int(y_str[index])
                if val <= 0:
                    return calculate_sum(index + 1, current_sum + val**4)
                else:
                    return calculate_sum(index + 1, current_sum)
            except IndexError:
                return "-1"
            except ValueError:
                return "-1"

        if len(y_str) != x:
            return "-1"
        return calculate_sum(0, 0)
    except ValueError:
        return "-1"

def main():
    try:
        n = int(input())

        def get_result(i, results_str):
            if i == n:
                print(f"{results_str[0]}\n{results_str[1:]}")
                return
            result = process_test_case()
            get_result(i + 1, results_str + result)

        get_result(0, "")

    except ValueError:
        pass

if __name__ == "__main__":
    main()