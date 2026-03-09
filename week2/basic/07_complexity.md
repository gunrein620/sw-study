# 알고리즘 복잡도 분석: 중복 원소 찾기 (complexity.py)

이 문서는 동일한 문제를 해결하는 세 가지 알고리즘의 시간 및 공간 복잡도를 분석한 내용을 정리합니다.

---

## 1. 알고리즘별 복잡도 요약

| 해결 방법 | 시간 복잡도 | 공간 복잡도 | 특징 |
| :--- | :--- | :--- | :--- |
| **방법 1: Brute Force** | $O(n^2)$ | $O(1)$ | 구현이 단순하지만 데이터가 많아질수록 성능이 급격히 저하됨 |
| **방법 2: Sorting** | $O(n \log n)$ | $O(1)$ | 데이터를 정렬한 후 인접 원소를 비교함. 추가 메모리가 거의 불필요 |
| **방법 3: Hash Set** | $O(n)$ | $O(n)$ | 가장 빠른 성능을 보이나, 데이터를 저장할 추가 공간이 필요함 |

---

## 2. 방법별 상세 분석 및 코드

### 방법 1: Brute Force (이중 반복문)
- **원리**: 모든 원소를 하나씩 선택하여 나머지 모든 원소와 대조합니다.
- **시간 복잡도**: $O(n^2)$ - 데이터가 $n$배 늘어나면 연산량은 $n^2$배 증가합니다.
- **공간 복잡도**: $O(1)$ - 결과를 담는 리스트 외에 고정된 변수만 사용합니다.

```python
def find_duplicates_brute_force(nums):
    duplicates = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                if nums[i] not in duplicates:
                    duplicates.append(nums[i])
    return duplicates
```

## 방법 2: Sorting (정렬 후 탐색)
- 원리: 배열을 정렬하면 동일한 원소들이 인접하게 배치되는 특성을 이용합니다.
- 시간 복잡도: $O(n \log n)$ - 파이썬 내부 정렬 알고리즘(Timsort)의 성능을 따릅니다.
- 공간 복잡도: $O(1)$ - 제자리 정렬(In-place sort)을 수행할 경우 추가 공간이 거의 없습니다.
```python
def find_duplicates_sorting(nums):
    if not nums: return []
    nums.sort()
    n = len(nums)
    duplicates = []
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            if nums[i] not in duplicates:
                duplicates.append(nums[i])
    return duplicates
```
### 방법 3: Hash Set (해시 집합)

- **원리**: `set` 자료구조를 사용하여 이미 확인한 원소를 $O(1)$ 시간에 조회합니다.
- **시간 복잡도**: $O(n)$ - 배열을 단 한 번만 순회하므로 효율이 가장 좋습니다.
- **공간 복잡도**: $O(n)$ - 원소 저장을 위해 `seen`과 `duplicates` 집합을 사용합니다.

```python
def find_duplicates_hash(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
