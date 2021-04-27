from django.core.management.base import BaseCommand
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from django.conf import settings
from bot.models import User, Product, Product_Group, Brand



class Command(BaseCommand):
    PAGE_LIMIT = 5
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.updater = Updater("1424464372:AAGIO9M97Z_0SsAVQaHKnQ0gzesj_5kt27M")

    def start(self, update: Update, context: CommandHandler):
        button1 = []
        for row in Product_Group.objects.order_by("-id").all():
            button1.append([InlineKeyboardButton(row.name, callback_data="pg{}".format(row.id))])
        self.updater.bot.send_message(chat_id=update.message.chat_id,
                                          text="Assalomu aleykum TEXNO_SHOP ga xush kelipsiz. Siz bu bot orqali maishiy texnikalar TELEVIZOR MUZLATGICH KONDINSANER CHANGYUTGICH KIRYUVADIGAN MASHINA xarit qilishingiz mumkun",
                                          reply_markup=InlineKeyboardMarkup(button1))

    def command_product_group(self, update: Update, context):
        id = int(update.callback_query.data[2:])
        try:
            product_group = Product_Group.objects.filter(id=id).get()
        except Product_Group.DoesNotExist:
            update.callback_query.answer("Malumot yoq")
            return
        button3 = []
        for row in Brand.objects.order_by("-id").all():
            button3.append([InlineKeyboardButton(row.brand_name, callback_data="b{}".format(row.id))])
        self.updater.bot.send_message(chat_id=update.callback_query.message.chat_id, text="Brand tanlang", reply_markup=InlineKeyboardMarkup(button3))
    def commadn_brand(self, update: Update, context):
        id = int(update.callback_query.data[1:])
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            update.callback_query.answer("Malumot yoq")
            return
        update.callback_query.answer()
        self.updater.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                      text="* {} * \n\n{}".format(product.subject, product.content))


    def handle(self, *args, **options):
        dispatcher = self.updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CallbackQueryHandler(self.command_product_group, pattern="^pg\d+$"))
        dispatcher.add_handler(CallbackQueryHandler(self.commadn_brand, pattern="^b\[0-9]+$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.callback_artel, pattern="artel"))

        self.updater.start_polling()
        self.updater.idle()
