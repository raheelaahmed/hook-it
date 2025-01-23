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

- **Homepage**

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

### Content

### Media



# bugs and fixes:

foreign key error in serch term

![foriegn-key-error](documents/screenshots/foriegn-key-error.png)

solution:

Since category is a foreign key, we can't filter it with icontains directly as if it were a CharField. we need to filter based on a field within the related Category model, like category__name__icontains.







