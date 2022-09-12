import logging
import time
from telegram import *
from telegram.ext import *
from PIL import Image

from train import model_construct
from image_processing import process_image


model = model_construct()


def start(update, context):
    update.message.reply_text('Wellcome to Amharic Digit Recognition bot\n Enter your drawing')

def error_message(update, context):
    update.message.reply_text("Send your drawing for prediction")
    
def predict(update, context):
    photo = update.message.photo
    images = []
    for image in photo:
        img = context.bot.getFile(image.file_id)
        path = f'image/{int(time.time() * 100)}_{image.file_unique_id}.png'
        img.download(path)
        images.append(path)
    data = images[0] # 4 different size images are recieved, index 0 is the minimum size among them 
    image = Image.open(data)
    x = process_image(image)
    if x is None:
        update.message.reply_text(
        "invalid image",
        reply_markup=ReplyKeyboardRemove())

        update.message.reply_text(
        "Send your drawing for prediction",
        reply_markup=ReplyKeyboardRemove())
        return 0

    
    prediction = model.predict(x)[0]
    classes = ['1', '10', '100', '10000', '2', '20', '3', '30', '4', '40', '5', '50', '6', '60', '7', '70', '8', '80', '9', '90']
    result = [(prediction[i], classes[i]) for i in range(20)]
    result.sort(reverse=1)
    accuracy = 100 * result[0][0]
    accuracy = accuracy * 10000 // 100 / 100
    threshold = 60
    print(accuracy, result[0][1])
    if accuracy >= threshold:
        update.message.reply_text(
            f"The predicted value is {result[0][1]} with a probability {accuracy:.2f}%",
            reply_markup=ReplyKeyboardRemove())
        update.message.reply_text(
            "Send your drawing for prediction",
            reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(
            "Please try again",
            reply_markup=ReplyKeyboardRemove())

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    persistence = PicklePersistence(filename='conversationbot')
    updater = Updater(token="5358758787:AAFT684iFOHIo4z7_X_nGi95dNC9xpM-CC8", persistence=persistence)
    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo | Filters.document.category("image"), predict))
    dispatcher.add_handler(MessageHandler(Filters.all, error_message))

    updater.start_polling()
    updater.idle()
    



if __name__ == '__main__':
    main()



# [
#     {
#         'file_unique_id': 'AQADdbkxG2dawFN4', 
#         'width': 51
#         'height': 90, 
#         'file_size': 648, 
#         'file_id': 'AgACAgQAAxkBAAIB0mJ3oJ2U55clQFTnJfYdNhD3ztdMAAJ1uTEbZ1rAU98TJCwCkRd7AQADAgADcwADJAQ', 
#     }, 
#     {
#         'file_unique_id': 'AQADdbkxG2dawFNy', 
#         'width': 180
#         'height': 320, 
#         'file_size': 4289, 
#         'file_id': 'AgACAgQAAxkBAAIB0mJ3oJ2U55clQFTnJfYdNhD3ztdMAAJ1uTEbZ1rAU98TJCwCkRd7AQADAgADbQADJAQ', 
#     }, 
#     {
#         'file_unique_id': 'AQADdbkxG2dawFN9', 
#         'width': 450
#         'height': 800, 
#         'file_size': 12462, 
#         'file_id': 'AgACAgQAAxkBAAIB0mJ3oJ2U55clQFTnJfYdNhD3ztdMAAJ1uTEbZ1rAU98TJCwCkRd7AQADAgADeAADJAQ', 
#     }, 
#     {
#         'file_unique_id': 'AQADdbkxG2dawFN-', 
#         'width': 720
#         'height': 1280, 
#         'file_size': 19917, 
#         'file_id': 'AgACAgQAAxkBAAIB0mJ3oJ2U55clQFTnJfYdNhD3ztdMAAJ1uTEbZ1rAU98TJCwCkRd7AQADAgADeQADJAQ', 
#     }    
# ]