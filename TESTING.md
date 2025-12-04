# **TESTING.md — Mathematics Learning Blog Testing Documentation**

---
---

# Testing

A full breakdown of all tests can be found in:

**[TESTING.md](TESTING.md)**

Testing includes:

* Automated Python tests
* Form validation tests
* Authentication tests
* Manual UI/UX testing
* Browser testing
* Accessibility testing
* HTML/CSS validation

---

# Mathematics Learning Blog — Testing

This file documents all testing practices performed for the project, fulfilling LO4.1–LO4.3.

---

# 1. Automated Python Tests

## 1.1 Model Tests

* Post model creates correctly
* Timestamps function
* Author relationship validated

## 1.2 View Tests

* Homepage loads with 200 status
* Blog detail view loads
* Dashboard requires login
* Create/Edit/Delete views require authentication
* Unauthorized attempts redirect appropriately

## 1.3 Form Tests

* Title required
* Content required
* Invalid submissions rerender with errors

## 1.4 Authentication Tests

* Valid login → redirects to dashboard
* Invalid login → displays error message
* Logout clears session

---

# 2. JavaScript Tests

*(Only if you include JS features)*

Possible tests:

* Form auto-validation
* Button behaviour
* Dynamic UI elements

---

# 3. Manual UX Testing

* All links tested
* Navigation works on all screen sizes
* Colours accessible
* Feedback messages appear correctly
* CRUD operations flow tested manually

---

# 4. Browser Compatibility

Tested on:

* Chrome
* Firefox
* Edge
* Safari

---

# 5. Accessibility Testing

Tools:

* Lighthouse
* Screen reader checks
* Keyboard navigation checks

This ensured:

* Good contrast
* Proper heading structure
* ARIA labels where needed

---

# 6. Code Validation

### HTML

Validated with W3C Markup Validator.

### CSS

Validated using W3C CSS Validator.

### Python

Checked with PEP8/flake8 linting.

---

# 7. Bug Tracking

| Bug     | Description                    | Fix                    |
| ------- | ------------------------------ | ---------------------- |
| Example | Incorrect redirect after login | Updated redirect logic |

Any remaining minor bugs are documented here.

---