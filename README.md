# Cats vs Dogs

### This project consists in a Computer Vision model capable of recognize wheter a picture contains a cat or a dog. 
I've chosen a simple implementation, made with Python 3.7, Flask framework, Jinja and HTML. I decided not to work a lot on the frontend development, as I felt it was more important to demonstrate how the model performs.

# Usage
[You can test the model here.](https://pets-vs-dogs.herokuapp.com)
You only need to upload a picture of a cat or a dog and then simply hit the 'upload' button.


# Future Imporvements
I've trained the code in Google Colab using Tensorflow 2.2, and acording to the validation accuracy, my model should have a 90% of accuracy.

Nevertheless, I've found the following issues:

  - If the object in the picture tends to the white color, the model will identify it as a cat
  - If the animal has big ears, the model will confuse it with a cat
  - The model tends to associate small snouts with cats

# ToDos:
  - Improve model's accuracy by retraining it with more diverse images
  - Improve the frontend
  - Turn the model into a multi label model so it can recognize more than one category inside each image
