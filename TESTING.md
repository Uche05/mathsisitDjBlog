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

Automated tests were written to verify core model behaviour:

* Post model instances create correctly
* Author–Post relationship is enforced
* Slug fields are auto-generated from titles
* Slugs remain unique when duplicate titles are used
* Timestamp fields populate correctly

All model tests passed successfully.

## 1.2 View Tests


The following view behaviours were tested using Django’s test client:

* Homepage loads successfully with HTTP 200
* Blog list page loads successfully
* Published blog detail pages return HTTP 200
* Draft blog posts return HTTP 404 for anonymous users
* Dashboard requires user authentication
* Create, Edit, and Delete views require authentication
* Non-authors cannot edit or delete posts they do not own

During testing, an initial failure occurred when attempting to access a draft
post as an anonymous user. This resulted in a 404 response, which was confirmed
to be correct behaviour based on the application’s access rules.

The test was updated to explicitly check:
- Published posts return HTTP 200
- Draft posts return HTTP 404 for unauthenticated users

After this correction, all view tests passed successfully.

## 1.3 Form Tests

Form validation was tested to ensure data integrity:

* Title field is required
* Content field is required
* Content length validation is enforced
* Invalid submissions do not create database records
* Validation errors are returned to the user correctly

All form tests passed successfully.


## 1.4 Authentication Tests

Authentication workflows were tested to confirm secure access:

* Valid login redirects the user correctly
* Invalid login attempts display error feedback
* Logout clears the authenticated session
* Protected routes redirect unauthenticated users

All authentication tests passed successfully.

### Test Execution

All automated tests were executed using Django’s test runner:

python manage.py test

A separate test database was created and destroyed automatically for each run,
ensuring isolation and repeatability of test results.


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

Manual testing has been performed and all have passed.

# 4. Browser Compatibility

Tested on:

* Chrome
* Firefox
* Edge
* Safari

The website works on all these browsers and is cross compatible to them.
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


# 6. Code Validation

### HTML

I could not continue validating with W3C Validator as it introduced errors due to it being a Django Template.


### CSS

Validated using W3C CSS Validator.

<img src="documentation/cssval.png" alt= "css validation passed">

### Python

Python code was validated using flake8 to ensure PEP8 compliance.

Initial linting identified issues such as:
- Line length violations
- Unused imports and variables
- Spacing and formatting inconsistencies
- Test file formatting issues

These were addressed where appropriate. Auto-generated migration files were
excluded from strict linting, as recommended by Django best practices.



# 7. Bug Tracking

| Bug | Description | Resolution |
|-----|------------|------------|
| Draft post returned 404 during testing | Anonymous user attempted to access draft post | Test updated to reflect correct access control |
| Missing dependency error during tests | WhiteNoise not installed locally | Added dependency to requirements |

All critical bugs discovered during development and testing were resolved.


Any remaining minor bugs are documented here.

---

## Testing Conclusion

All core application functionality has been verified through a combination of
automated and manual testing. CRUD operations, authentication, permissions,
and data validation behave as expected.


