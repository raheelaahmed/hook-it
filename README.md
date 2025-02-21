# [Hook It](https://hook-it-85e92c23978c.herokuapp.com/)

Hook It is an online platform that offers a wide range of crochet patterns for enthusiasts of all skill levels. Designed for individuals who love crocheting and are looking for creative patterns to bring their projects to life, the website features a variety of crochet designs, including hats, scarves, shawls, baby booties, blankets, amigurumi, and more.

Users can browse through different patterns, select the ones they like, and easily purchase them. After purchasing, users will be able to download a comprehensive PDF, which includes step-by-step instructions, materials required, and detailed guidance to help them complete their project from start to finish. Whether you're a beginner or an experienced crocheter, Hook It makes it simple to dive into your next crochet creation with clear and accessible patterns.
## UX

### ER diagram:
I have created an Entity-Relationship (ER) diagram that visually represents the relationships between all the data models used in the application. The diagram provides an overview of how the different entities within the system are structured and how they relate to each other.

* The primary entitiesclude User, UserProfile, Category, Pattern, and Review.

* User and UserProfile: The UserProfile model is linked to the User model with a one-to-one relationship, where each user can have only one profile. The profile stores additional information such as the user's default address, phone number, and country.

* Category and Pattern: The Pattern model is related to the Category model via a foreign key, meaning each pattern belongs to a specific category (e.g., 'Beginner', 'Intermediate', 'Advanced'). This relationship allows patterns to be categorized for better organization.

* Pattern and Review: There is a one-to-many relationship between Pattern and Review. Each pattern can have multiple reviews, but each review is associated with only one pattern. The Review model stores feedback from users, including ratings and comments.

* User and Review: The Review model is also linked to the User model, where a user can leave multiple reviews, but each review is written by only one user. This relationship helps track user-generated content and feedback for patterns.

This ER diagram enables a clear understanding of the data structure and how entities within the system are connected, facilitating easier database management and querying. The relationships reflect how the data models are interdependent and how data flows between them to support application functionality.

![ER-Diagram](documents/screenshots/ER-diagram.png)
### Colour Scheme:

For my project, I’ve chosen a well-balanced color scheme that combines subtle tones with a professional, clean look. For the text color, I opted for a slightly darker shade of grey. This choice enhances readability while maintaining a modern and sophisticated feel. The darker grey provides sufficient contrast against the lighter background, ensuring that the content is easy to read without being too harsh or overwhelming, as black text might be. This approach allows for a more refined, comfortable user experience, while also contributing to the overall aesthetic of the design.


![](documents/screenshots/hook-it.png)


### Typography
 
 I have font awesome fonts and icons on my app.

## User Stories:

* User can view explore patterns.
* User can open the pattern and can see pattern detail.
* User can add the pattern to bag using add to bag feature on pattern detail page.
* User can review the pattern on pattern detail page.
* User can Edit and Delete his review.
* User can see if they have anything in the bag by looking at bag icon in the nav bar, if they have patterns in the basket bag will show total amount payable. 
If bag is empty they can see amout 0.00.
* User can open the bag to see what is in the bag.
* User can delete the pattern from the bag.
* User can go checkout securely from the shopping bag page.
* user can return back to pattern page to exple more pattern from shopping bag page.
* User can do a secure checkout using stipe payment form.
* User can see oder detail as well.
* User can acess pattern download link if the payment was successfull.
* User can download the pattern.
* User can contact the administration if they have any problem with patterns using contact us form from the nav bar.
* User can see all his order on his profile, he can see it in the nav bar if he in signed in.
* User can access pattern by clicking order number from profile page. He will access the checkout sucess page from where he can download pattern agin.
* User can Sign up using sign up form.
* User can sign in if thgey have already an account.
* User can logout using logout form.
* User can see his status if he is signbed in or sign out by looking at nav bar. It cahngeds accordingly.
* User can reset the password if they forgot using a button on sign in page.
* User recieves authentication email for secure signup process.

## Admin Stories:

* Admin can access extra feaures form managing the app.
* Admin can add a Pattern using a front end form. he can acess the form from the nav bar named Pattern Management.
* Admin can Edit and delete the pattern as well using edit and delete buttons on pattern and pattern detail page.
* Admin recieves email from the user, if user tryies to contact using contact us form.
* Admin can edit and delete user reviews using frontend as well.


### Site Pages

- **Home page**


The homepage features a clean and minimalist design. At the top, there is a navigation bar that includes the logo on the left-hand side and links and button on the right-hand side for other pages and actions. The central part of the page showcases a prominent slogan, clearly communicating the brand’s message or theme. Below the slogan, there is a call-to-action button inviting users to "Explore the Patterns," encouraging them to engage with the content further. This simple yet effective layout creates a user-friendly experience while keeping the focus on the essential elements of the page.

![Home](documents/screenshots/home.png)

- **About page**


The About page provides users with an introduction to the platform, explaining who we are and what we offer. It gives a brief overview of crochet, its origins, and its creative potential. The page highlights the various projects and items that can be made using crochet, from decorative pieces to practical accessories, showcasing the versatility and artistry of this craft. This section aims to inspire visitors and give them a deeper understanding of crochet and its endless possibilities.

![About](documents/screenshots/about.png)

- **Patterns page**
The Patterns page showcases a variety of crochet patterns, displaying images, names, prices, and ratings for each one. Users can easily explore the available patterns, with each pattern name linked to its detailed page for more information. Additionally, the page offers sorting options, allowing users to filter patterns by name, date, or price, making it easier to find the perfect pattern based on their preferences.

![patterns](documents/screenshots/patterns.png)

- **Pattern-detail page**

The pattern detail page provides comprehensive information about the pattern, including the materials required and the available sizes that can be made using it. Users who are logged in can rate the pattern and leave reviews. The page displays key details such as the pattern name, difficulty level, price, and a quantity input field. There are also options to add the pattern to the shopping cart or continue shopping. Below the product description, logged-in users can share their feedback by leaving a rating and review of the pattern.

![pattern-deatil](documents/screenshots/pattern-detail.png)

- **contact-us page**

The Contact Us page allows users to reach out to the administration for any issues they may encounter. Messages submitted through the page will be sent to the admin panel as well as the administration's email address.

![contact-us](documents/screenshots/contact-us-screenshot.png)

- **Profile page**


The profile page displays a user's biodata, which can be updated using the provided form. It also includes the user's order history, allowing them to view purchased patterns by clicking on the order number. By selecting an order number, users can revisit the checkout success page and access the download link for their purchased pattern.

![Profile](documents/screenshots/profile-screenshot.png)

- **Pattern management page**


This page is exclusively accessible to the management team, providing a frontend form for adding new patterns. If a user is logged in and is a member of the administration, they will see the Pattern Management option in the navigation bar, allowing them to add new patterns to the Patterns page.

![add_pattern](documents/screenshots/add-pattern-screenshot.png)

- **Edit pattern page**

This page is also designed for the administration. An Edit button is available on both the Patterns and Pattern Detail pages, allowing admins to easily update pattern information.

![edit-pattern](documents/screenshots/edit-pattern-screenshot.png)


- **Shopping Bag page**

This is the Shopping Bag page, where users can view all the patterns they have added to their bag. Each pattern displays five details: Pattern Image, Pattern Name, Price, a Remove button to delete the pattern, and the Subtotal. Users can remove a pattern from the bag using the Remove button. Additionally, they can continue shopping by clicking the Keep Shopping link or proceed to checkout by selecting Secure Checkout.

![shopping-bag](documents/screenshots/shopping-bag-screenshot.png)


- **checkout page**

This is the Checkout page, where users can complete their purchase using the Stripe payment system. The page is divided into two sections: the left side contains the payment form, where users enter their details, and the right side displays the order summary, including order details and the total amount. Once the correct information is provided, users can successfully complete their checkout.


![checkout](documents/screenshots/checkout-screenshot.png)



- **Checkout Success page**


This is the Checkout Success page, confirming that your order has been completed. A confirmation email with order details has been sent to you. The page displays your order summary along with a download link for your purchased pattern. Additionally, a "Check Out Our Latest Deals!" button is provided, allowing you to return to the patterns page and continue shopping.


![checkout-success](documents/screenshots/chekout-success-screenshot.png)


- **Order Confirmation Email**

The user will receive a confirmation email containing the details of their order, including the order summary and payment confirmation.


![email](documents/screenshots/email-screenshot.png)


- **Privacy Policy**


This page contains the privacy policy for our app. A link to this page is available in the footer for easy access.


![Privacy-Policy](documents/screenshots/privacy-Policy-sceenshot.png)


### Allauth Templates:

- **Sign-in page**

![Sign-In](documents/screenshots/sign-in-screenshot.png)
- **Sign-out page**

![Sign-out](documents/screenshots/signout-screenshot.png)
- **Sign-up page**

![Sign-Up](documents/screenshots/signup-form-screenshot.png)


#### Password Reset Process:












### User Features

- **Review and Rating**

Users have the opportunity to share their feedback by rating and reviewing the pattern. This allows others to get insights based on real experiences, helping them make more informed decisions before purchasing.

![Review](documents/screenshots/review.png)



- **pagination**

The patterns page includes a pagination feature, allowing users to easily navigate through multiple pages of patterns without having to scroll endlessly. Users can view a set number of patterns per page and click the "Next Page" button to explore more options. If they wish to go back, they can simply click the "Previous" button to return to the previous page.

![Pagination](documents/screenshots/pagination.png)


- **Sorting**

The pattern page offers a sorting feature that allows users to organize the patterns based on their preferences. Users can sort the patterns by the newest arrivals, price (from highest to lowest or lowest to highest), and alphabetically (from A to Z or Z to A). This makes it easier to find patterns that meet specific criteria.

![Sorting](documents/screenshots/sorting.png)

- **Search**

The search feature allows users to easily find patterns by entering keywords, whether it’s the pattern name, a specific term from the description, or a category. This makes it simple for users to quickly locate the exact pattern they're looking for.

![Seearch](documents/screenshots/search.png)





- **Toasts**



- **Bag Updates**


- **User Email Confirmations**

- **Course Sort**

- **Course Search**

- **Newsletter Subscribe**

- **Newsletter Unsubscribe**

### Admin Features

- **Webhooks**

### Future Features

## Testing

#### Cloning

## Credits

* https://www.flaticon.com   (logo)
* https://coolors.co/
* https://www.youtube.com/watch?v=wY_BNsxCEi4
i have followed this video for adding pagination.
* https://www.youtube.com/watch?v=J-r75L3Tflg
i have followed this video for kepping the footer at the botom of page without using fixed or stickey position.
* https://dbdiagram.io/ .
* https://mailchimp.com/?currency=EUR
created ER diagram
### Content

### Media



# bugs and fixes:

foreign key error in serch term

![foriegn-key-error](documents/screenshots/foriegn-key-error.png)

solution:

Since category is a foreign key, we can't filter it with icontains directly as if it were a CharField. we need to filter based on a field within the related Category model, like category__name__icontains.


## Error redirect error:

Redirect error for clicking add to bag button.

![Redirect-error](documents/screenshots/redirect.png)

Solution:

Import Redirect from django shortcuts.

## Cispy_form error:

Crispy_form error :

![crispy](documents/screenshots/crispy-form.png)

Solution:

added 'crispy_bootstrap4' in installed apps to fix it.


## stripe card input field disabled:

Issue: On the checkout page, the payment card input field was disabled due to an insecure form connection.

Solution: I resolved this issue by clearing the browser history and cache, which allowed the form to reload securely.


## problem with media files:

Issue: I was unable to view media files, such as the logo, background, and other images, on my app.

![Home-page-with-bug](documents/screenshots/bug-home.png)


Solution: After removing the SSL configuration from the settings, everything started working properly.

![fixed-homepage](documents/screenshots/fiexed-home.png)










