# **Coverage Report**

### **Code Coverage Summary**
| Name               | Statements | Missed | Coverage |
|--------------------|------------|--------|----------|
| `functions.py`     | 131        | 1     | 99%      |
| **Total**          | 131        | 1     | 99%      |

### **Remarks**
- **Current Coverage**: 78%
---

## **Testing Overview**

### **What Has Been Tested and How?**
- **Unit Testing**: 
  - Most functions have been tested individually to verify their behavior and expected outputs.
  - Some functions do not have specific unit tests but are indirectly tested through higher-level tests.
- **End-to-End Testing**:
  - Full system functionality has been tested to ensure integration and correctness of workflows.

---

### **Test Input Types**
- **Usual Inputs**:
  - Regular inputs expected during normal usage.
- **Wrong Type**:
  - Inputs with incorrect types to validate error handling.
- **Invalid Values**:
  - Out-of-range values, e.g., `128` when the maximum allowable value is `127`.
- **Edge Cases**:
  - Scenarios that test the boundaries of input validity.

---

### **How to Repeat the Tests**
1. **Run Unit Tests**:
      poetry run python -m coverage run -m unittest

2. **Run Coverage Report**:

   poetry run python -m coverage report -m
