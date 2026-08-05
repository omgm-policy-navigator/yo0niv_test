from policy_navigator.domain.policy import CategoryCode, EvaluationStatus


def test_mvp_category_codes_are_defined() -> None:
    assert [category.value for category in CategoryCode] == [
        "HOUSING",
        "LOAN",
        "WEDDING",
        "TAX",
        "CHILDCARE",
    ]


def test_mvp_evaluation_statuses_are_defined() -> None:
    assert EvaluationStatus.NEEDS_CONFIRMATION.value == "NEEDS_CONFIRMATION"
