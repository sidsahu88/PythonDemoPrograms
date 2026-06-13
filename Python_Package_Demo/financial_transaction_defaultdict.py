from collections import defaultdict


def highest_withdrawal(transactions: list) -> int:
    withdrawals = defaultdict(int)

    for transaction in transactions:
        tran_date, user_id, amount, tran_type = transaction.split(",")

        if tran_type == "WITHDRAW":
            tran_date = tran_date.split('T')[0]
            withdrawals[(tran_date, user_id)] += int(amount)

    max_withdrawals = -1
    result_user = None

    for (_, wuser_id), tot_amt in withdrawals.items():
        if tot_amt > max_withdrawals:
            max_withdrawals = tot_amt
            result_user = int(wuser_id)
        elif tot_amt == max_withdrawals:
            if result_user > int(wuser_id):
                result_user = int(wuser_id)

    return result_user


if __name__ == "__main__":
    test_cases = [
        {
            "name": "Tie-breaker",
            "data": ["2024-05-01T10:00:00,200,1000,WITHDRAW", "2024-05-01T10:00:00,100,1000,WITHDRAW"],
            "expected": 100
        },
        {
            "name": "Mixed Types",
            "data": ["2024-05-01T10:00:00,102,2000,DEPOSIT", "2024-05-01T11:00:00,101,500,WITHDRAW"],
            "expected": 101
        }
    ]

    for tc in test_cases:
        actual = highest_withdrawal(tc["data"])
        print(
            f"Test {tc['name']}: {'PASS' if actual == tc['expected']
                                  else 'FAIL (Got ' + str(actual) + ' but Expected ' + str(tc['expected']) + ')'}")
