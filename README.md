# [Hook It]

Hook It is an online platform that offers a wide range of crochet patterns for enthusiasts of all skill levels. Designed for individuals who love crocheting and are looking for creative patterns to bring their projects to life, the website features a variety of crochet designs, including hats, scarves, shawls, baby booties, blankets, amigurumi, and more.

Users can browse through different patterns, select the ones they like, and easily purchase them. After purchasing, users will be able to download a comprehensive PDF, which includes step-by-step instructions, materials required, and detailed guidance to help them complete their project from start to finish. Whether you're a beginner or an experienced crocheter, Hook It makes it simple to dive into your next crochet creation with clear and accessible patterns.
## UX
### Colour Scheme:

For my project, I’ve chosen a well-balanced color scheme that combines subtle tones with a professional, clean look. For the text color, I opted for a slightly darker shade of grey. This choice enhances readability while maintaining a modern and sophisticated feel. The darker grey provides sufficient contrast against the lighter background, ensuring that the content is easy to read without being too harsh or overwhelming, as black text might be. This approach allows for a more refined, comfortable user experience, while also contributing to the overall aesthetic of the design.


![](documents/screenshots/hook-it.png)


### Typography
## User Stories
## Features

### Existing Features

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

### User Features

- **Toasts**

- **Basket Updates**


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








