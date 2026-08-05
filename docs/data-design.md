# 데이터 설계

## 설계 원칙

MVP에서는 정책 추천과 설명에 필요한 최소 테이블만 둔다. 정책 변경 이력, 생애 이벤트, 관리자 검수 이력은 요구가 구체화된 뒤 별도 테이블로 확장한다.

## 핵심 테이블

### 1. `category`

5개 정책 분야를 저장한다.

```text
category
- id
- code
- name
- description
- display_order
```

초기 코드:

```text
HOUSING
LOAN
WEDDING
TAX
CHILDCARE
```

### 2. `policy`

정책 기본 정보와 RAG에 사용할 설명의 기준 정보를 저장한다.

```text
policy
- id
- category_id
- name
- summary
- managing_agency
- application_url
- application_start_date
- application_end_date
- status
- source_url
- verified_at
```

MVP에서는 정책 버전 테이블을 분리하지 않는다. 정책 변경 이력을 반드시 사용자에게 보여줘야 하는 단계에서 `policy_version`을 추가한다.

### 3. `policy_rule`

정책 자격 조건을 저장한다.

```text
policy_rule
- id
- policy_id
- condition_key
- operator
- expected_value
- required
- question_id
- source_text
```

예시:

```text
policy_id: 1
condition_key: RESIDENCE_REGION
operator: EQ
expected_value: SEOUL
required: true
```

```text
policy_id: 1
condition_key: HOME_OWNERSHIP
operator: EQ
expected_value: HOUSELESS
required: true
```

### 4. `question`

분야별 질문을 저장한다.

```text
question
- id
- category_id
- condition_key
- question_text
- answer_type
- options
- priority
- parent_question_id
- show_condition
```

예시:

```text
question_text: 두 분 모두 무주택인가요?
condition_key: HOME_OWNERSHIP
answer_type: SINGLE_SELECT
options: ["예", "아니오", "잘 모르겠어요"]
```

`show_condition`은 조건부 질문에 사용한다.

```text
자녀가 있다고 응답한 경우에만
자녀 생년월일 질문 표시
```

### 5. `user_fact`

사용자가 답변한 조건을 저장한다.

```text
user_fact
- id
- condition_key
- value
- source
- updated_at
```

예시:

```text
condition_key: MARRIAGE_STATUS
value: PRE_MARRIED
```

```text
condition_key: RESIDENCE_REGION
value: SEOUL
```

### 6. `policy_evaluation`

사용자별 정책 판정 결과를 저장한다.

```text
policy_evaluation
- id
- policy_id
- result_status
- matched_conditions
- missing_conditions
- failed_conditions
- recommendation_score
- evaluated_at
```

상태:

```text
LIKELY_ELIGIBLE
NEEDS_CONFIRMATION
AVAILABLE_LATER
LIKELY_INELIGIBLE
OFFICIAL_CONFIRMATION_REQUIRED
```

### 7. `policy_relation`

정책 간 관계와 신청 순서를 저장한다.

```text
policy_relation
- id
- from_policy_id
- to_policy_id
- relation_type
- description
```

관계:

```text
BEFORE
AFTER
RELATED
ALTERNATIVE
CONFLICT
REEVALUATE_AFTER
```

예시:

```text
혼인신고
→ REEVALUATE_AFTER
→ 결혼세액공제
```

생애단계를 정책이 아닌 별도 이벤트로 관리하고 싶다면 이후 `life_event` 테이블을 추가할 수 있다.

## RAG 최소 데이터

MVP에서는 정책별 원문을 다음 정도로 관리한다.

```text
policy_document
- id
- policy_id
- document_type
- title
- content
- source_url
- embedding
```

`document_type`:

```text
OVERVIEW
ELIGIBILITY
APPLICATION
DOCUMENTS
FAQ
CAUTION
```

PostgreSQL의 `pgvector`를 사용하면 별도 Vector DB를 두지 않아도 된다.

