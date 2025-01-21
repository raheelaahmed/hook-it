# [Hook It]
## UX
### Colour Scheme
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

### Content

### Media



# bugs and fixes:

foreign key error in serch term

![foriegn-key-error](documents/screenshots/foriegn-key-error.png)

solution:

Since category is a foreign key, we can't filter it with icontains directly as if it were a CharField. we need to filter based on a field within the related Category model, like category__name__icontains.







