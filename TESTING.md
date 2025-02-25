# Testing

Return back to the [README.md](README.md) file.


## Code Validation


### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.


| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| 404 |![screenshot](documents/html-validation/error404.png) | Pass: No Errors |
| about | ![screenshot](documents/html-validation/about.png) | Pass: No Errors |
| add-pattern |  ![screenshot](documents/html-validation/about.png) | Pass: No Errors |
| bag | ![screenshot](documents/html-validation/bag.png) | Pass: No Errors |
| checkout |  ![screenshot](documents/html-validation/checkout.png) | Pass: No Errors |
| checkout-success |  ![screenshot](documents/html-validation/checkout-success.png) | Pass: No Errors |
| contact |  ![screenshot](documents/html-validation/contact-us.png) | Pass: No Errors |
| patterns | ![screenshot](documents/html-validation/patterns.png) | Pass: No Errors |
| edit-pattern | ![screenshot](documents/html-validation/edit-pattern.png) | Pass: No Errors |
| delete-confirm | ![screenshot](documents/html-validation/confirm-delete.png) | Pass: No Errors |
| home |  ![screenshot](documents/html-validation/home.png) | Pass: No Errors |
| login |  ![screenshot](documents/html-validation/signin.png) | Pass: No Errors |
| pattern-detail |  ![screenshot](documents/html-validation/pattern-detail.png) | Pass: No Errors |
| profile |![screenshot](documents/html-validation/profile.png) | Pass: No Errors |
| register |  ![screenshot](documents/html-validation/signup.png) | Pass: No Errors |
| sign-out |  ![screenshot](documents/html-validation/signout.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.


| File | Screenshot | Notes |
| --- | --- | --- |
| base.css | ![screenshot](documents/css-validation/bass-css.png) | Pass: No Errors( input base.css code passed but there are errors from external css fields given below) |
| external css | ![screenshot](documents/css-validation/external-css.png) | Fail: external css files like bootstrap,chimpmonk mail causing errors|
| checkout.css | ![screenshot](documents/css-validation/checkout.png) | Pass: No Errors |
| profile.css |  ![screenshot](documents/css-validation/profile.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documents/javascript-testing/stripe.png) | warning (use version 6)|
| countryfield.js | ![screenshot](documents/javascript-testing/contry-field.png) | Pass: No Errors |
| quantity-input-script.js | ![screenshot](documents/javascript-testing/qauntity-input.png) | warning (use version 6) |



### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

### Bag App
| File |  Screenshot | Notes |
| --- | --- | --- |
| apps.py | ![screenshot](documents/python-testing/apps.bag.png) | Pass: No Errors |
| contexts.py | ![screenshot](documents/python-testing/context.bag.png) | Pass: No Errors |
| urls.py |![screenshot](documents/python-testing/urls.bag.png) | Pass: No Errors |
| views.py |  ![screenshot](documents/python-testing/views.bag.png) | E501(line too long)|

### Checkout App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | ![screenshot](documents/python-testing/admin.checkout.png) | Pass: No Errors |
| apps.py | ![screenshot](documents/python-testing/apps.checkout.png) | Pass: No Errors |
| forms.py | ![screenshot](documents/python-testing/forms.checkout.png) | line too long |
| models.py | ![screenshot](documents/python-testing/models.checkout.png) | line too long, no newline at the end.|
| signals.py | ![screenshot](documents/python-testing/signals.checkout.png) | no new line |
| urls.py |![screenshot](documents/python-testing/urls.checkout.png) | line too long |
| views.py |![screenshot](documents/python-testing/views.checkout.png) | Pline too long |
| webhook_handler.py |![screenshot](documents/python-testing/wh-handler.checkout.png) | line too long, no new line |
| webhooks.py |  ![screenshot](documents/python-testing/wh.checkout.png) | line too long |


### Hook_It App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| asgi.py | ![screenshot](documents/python-testing/asgi.hookit.png) | Pass: No Errors |
| settings.py |  ![screenshot](documents/python-testing/setting.hookit.png) | line too long |
| urls.py |  ![screenshot](documents/python-testing/urls.hookit.png) | line too long |
| views.py |  ![screenshot](documents/python-testing/views.hookit.png) | Pass: No Errors |
| wsgi.py | ![screenshot](documents/python-testing/wsgi.hookit.png) | Pass: No Errors |

### Contact App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py |  ![screenshot](documents/python-testing/admin.contact.png) | line too long |
| apps.py | ![screenshot](documents/python-testing/apps.contact.png) | Pass: No Errors |
| models.py | ![screenshot](documents/python-testing/model.contact.png) | Pass: No Errors |
| urls.py |  ![screenshot](documents/python-testing/urls.contact.png) | Pass: No Errors |
| views.py | ![screenshot](documents/python-testing/views.contact.png) | line too long |



### Home App
| File |  Screenshot | Notes |
| --- |  --- | --- |
| apps.py |![screenshot](documents/python-testing/app.home.png) | Pass: No Errors |
| urls.py |  ![screenshot](documents/python-testing/urls.home.png) | Pass: No Errors |
| views.py |  ![screenshot](documents/python-testing/views.home.png) | line too long |


### Patterns App
| File |  Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](documents/python-testing/admin.pattern.png) |line too long |
| apps.py | ![screenshot](documents/python-testing/apps.pattern.png) | Pass: No Errors |
| forms.py |  ![screenshot](documents/python-testing/forms.pattern.png) | line too long |
| models.py |  ![screenshot](documents/python-testing/models.patterns.png) | Pass: No Errors |
| urls.py |  ![screenshot](documents/python-testing/urls.pattern.png) | Pass: No Errors |
| views.py |  ![screenshot](documents/python-testing/views.patterns.png) | line too long|

### Profiles App
| File |  Screenshot | Notes |
| --- | --- | --- |
| admin.py |  ![screenshot](documents/python-testing/admin-profile.png) | Pass: No Errors |
| apps.py |  ![screenshot](documents/python-testing/apps-profile.png) | line too long |
| forms.py | ![screenshot](documents/python-testing/form-profile.png) | line too long|
| models.py |  ![screenshot](documents/python-testing/models-profile.png) | line too long |
| urls.py |  ![screenshot](documents/python-testing/views-profile.png) | line too long|
| views.py |  ![screenshot](documents/python-testing/views-profile.png) | line too long |

### Root Level Files
| File | Screenshot | Notes |
| --- | --- | --- |
| custom_storages.py | ![screenshot](documents/python-testing/custom-storage.png) | Pass: No Errors |
| manage.py | ![screenshot](documents/python-testing/manage-py.png) | Pass: No Errors |



## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documents/browser/chorome.png) | Works as expected |
| Safari | ![screenshot](documents/browser/safari.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (googl3-pixel-7) | ![screenshot](documents/responsiveness/google-pixel-7.png) | Works as expected |
| Tablet (ipad-air) | ![screenshot](documents/responsiveness/ipad-air.png) | Works as expected |
| Mac-book | ![screenshot](documents/responsiveness/macbook.png) | Works as expected |
| XL Monitor | ![screenshot](documents/responsiveness/large-monitor.png) | Works as expected |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

On all pages, Lighthouse is flagging a warning 'Issues were logged in the Issues panel in Chrome Devtools'. This is caused by the built-in Stripe element used by the site.

| Page | Desktop | Notes |
| --- |  --- | --- |
| 404 | ![screenshot](documents/lighthouse-audit/error404.png) | pass |
| about |![screenshot](documents/lighthouse-audit/about.png) | pass |
| add-patern |  ![screenshot](documents/lighthouse-audit/add-a-pattern.png) | pass |
| bag | ![screenshot](documents/lighthouse-audit/add-a-pattern.png) | pass |
| checkout | ![screenshot](documents/lighthouse-audit/checkout.png) | pass |
| checkout-success |  ![screenshot](documents/lighthouse-audit/checkout-success.png) | pass |
| contact |  ![screenshot](documents/lighthouse-audit/contact-us.png) | pass |
| patterns | ![screenshot](documents/lighthouse-audit/patterns.png) | pass|
| edit-pattern |  ![screenshot](documents/lighthouse-audit/edit-pattern.png) | pass |
| confirm-delete |  ![screenshot](documents/lighthouse-audit/confirm-delete.png) | pass |
| home |  ![screenshot](documents/lighthouse-audit/home.png) |pass|
| sign-in |  ![screenshot](documents/lighthouse-audit/sign-in.png) | pass |
| pattern-detail |  ![screenshot](documents/lighthouse-audit/pattern-detail.png) | pass|
| profile | ![screenshot](documents/lighthouse-audit/profile.png) |pass|
| sign-up | ![screenshot](documents/lighthouse-audit/sign-up.png) |pass |
| sign-out | ![screenshot](documents/lighthouse-audit/signout.png) | pass |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on site name in navbar | Redirection to Home page | Pass | |
| | Click on About Us link in navbar | Redirection to About page | Pass | |
| | Click on Patterns link in navbar | Redirection to Patterns page | Pass | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Click on Search link in navbar | Search box dropdown, with input to search on Pattern page | Pass | |
| | Click on Register link in navbar | Redirection to Register page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on Bag link in navbar | Redirection to Bag page | Pass | |
| | Click on Profile link in navbar | Redirection to User Profile page | Pass | |
| | Click on Logout link in navbar | Redirection to Logout page | Pass | |
| | Click on Pattern Management link in navbar | Redirection to Add Pattern page | Pass | |
| | Click on Home link in navbar | Redirection to Home Page | Pass | |
| Footer | | | | |
| | Click on About Us link in footer | Redirection to About page | Pass | |
| | Click on Contact Us link in footer | Redirection to Contact page | Pass | |
| | Click on Privacy policy link in footer | Redirection to Privacy pocliy page | Pass | |
| | Click on 'Subscribe to our mailing list' button in footer | subscribtion essage | Pass | |
| Register | | | | |
| | Enter valid email address (twice) | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Redirects user to blank Login page | Pass |
| | Click on Back To Login button | Redirects user to Login page | Pass |
| Log In | | | | |
| | Enter valid username/email | Field will accept username or email format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Log user in, Redirects to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Logs out user, Redirects user to home page | Pass |
| Profile | | | | |
| | Click on the Update Information button | Inputted information is saved | Pass | |
| | Click on Order History links | Redirects to user order confirmation/checkout success page | Pass | |
| Site Navigations - Logged Out User | | | | |
| | Navigate to any login required URL | Redirect to login page, redirect back after login | Pass | |
| Pattern | | | | |
| | Click on Patterrn title | Redirect to clicked pattern details page | Pass | |
| | Click on sorting dropdown options | Sort patterns by selected criteria | Pass | |
| Patterns - Admin Only| | | | |
| | Click on an edit button | Redirect to edit pattern page for that pattern | Pass | |
| | Click on a delete button | directs to confirm delete page | Pass | |
| Pattern Details | | | | |
| | Click on 'Keep Shopping' button | Redirect to pattern page | Pass | |
| | Click on 'Add To Bag' button | Adds pattern to bag, bag message displayed | Pass | |
| | Click on 'submit Review' button | posts Review, success message displayed | Pass | |
| Pattern Details - Admin Only | | | | |
| | Click on Edit button | Redirect to edit pattern page for that pattern | Pass | |
| |  Click on delete button | directs to confirm-delete page| Pass | |
| |  Click on edit button for reviews|Redirect to edit review page for that review | Pass | |
| |  Click on delete button | delete the review | Pass | |
| Contact | | | | |
| | Email input | Required, accepts only email format | Pass | |
| | Subject input | Required, user given a list of options | Pass | |
| | Message input | Required | Pass | |
| | Click on 'Submit' button |Success message | Pass | |
| Add New Pattern - Admin Only | | | | |
| | Category Input | Not required, select from options | Pass | |
| | Difficulty Input | Not required, select from options | Pass | |
| | Name Input | Required | Pass | |
| | Price Input | Required, Numbers only | Pass | |
| | Date-Created | auto fill | Pass | |
| | Image | required | Pass | |
| | pattern URL |  required | Pass | |
| | Description Input | Required | Pass | |
| | Click on 'Cancel' button | Redirect to Pattern page | Pass | |
| | Click on 'Update Pattern' button | Save changes, redirect to pattern details page | Pass | |
| Delete Pattern - Admin Only | | | | |
| | Delete button | deletes the pattern | Pass | |
| Bag | | | | |
| | Click on 'Remove' link | Remove item from bag | Pass | |
| | Click on 'Keep Shopping' button | Redirect to Patterns page | Pass | |
| | Click on 'Secure Checkout' button | Redirect to Checkout page | Pass | |
| Checkout | | | | |
| | Full Name Input | Required | Pass | |
| | Email Input | Required, autofill if saved | Pass | |
| | Phone Number Input | Required, autofill if saved | Pass | |
| | Street Address 1 Input | Required, autofill if saved | Pass | |
| | Street Address 2 Input | Not required, autofill if saved | Pass | |
| | Town Or City Input | Required, autofill if saved | Pass | |
| | County Input | Not required, autofill if saved | Pass | |
| | Postal Code Input | Not required, autofill if saved | Pass | |
| | Country Input | Required, autofill if saved, select from options | Pass | |
| | Stripe Card Details | Required, validates on input | Pass | |
| | Check 'save delivery info.' box | Saves information to user profile | Pass | |
| | Click on 'Adjust Bag' button | Redirect to Bag page | Pass | |
| | Click on 'Complete Order' button | Complete Checkout with given information, redirect to order confirmation page if valid | Pass | |
| Newsletter - Subscribe | | | | |
| | Email Input | Required | Pass | |
| | Click on 'Subscribe' button | Subscribes user| Pass | |


