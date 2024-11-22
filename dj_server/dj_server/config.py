from datetime import timedelta

TZ_OFFSET = timedelta(hours=3)

TITLE = 'AutoCustomersStore'
BOT_LINK="tg://resolve?domain=autocosmeticsstore_bot"

# Define bot configuration constants
URL = "https://ef6f-178-124-178-90.ngrok-free.app"
ADMIN_CHAT_ID = 542399495 # @zamezamo
PORT = 8000
TOKEN = "7000362389:AAFGsZk51Japmkc_U6cXqmHM3IFOPo8eCI0"  # KEEP IT IN SECRET!

START_TEXT = (
    f"Добро пожаловать в *{TITLE}*!\n"
    f"Подписывайтесь на наш [канал]({BOT_LINK})!\n"
    f"\n"
    f"описание\nописание\nописание\nописание\n"
    f"\n"
)

START_OVER_TEXT = (
    f"*{TITLE}*\n"
    f"Подписывайтесь на наш [канал]({BOT_LINK})!\n"
    f"\n"
    f"описание\nописание\nописание\nописание\n"
    f"\n"
)

ADMIN_PANEL_TEXT = (
    f"*{TITLE}*\n"
    f"*[admin панель]*\n"
    f"_успешно авторизовано_\n\n\n"
)

PARTS_IN_CART_START_TEXT = (
    f"\n_в корзине присутствуют товары_"
)

CHOOSE_CATEGORY_TEXT = (
    f"\n_выберите категорию товара ниже:_"
)

EMPTY_TEXT = (
    f"здесь пусто.."
)

ENTER_PARTS_COUNT_TEXT = (
    f"введи количество товара, которое хочешь добавить в корзину\n\n"
    f"*0* - _удалить из корзины_"
)

PART_DELETED_FROM_CATALOG_ERROR_TEXT = (
    f"\n⚠️ *произошла ошибка*\n"
    f"_вот так совпадение, товар только что был убран из каталога_\n"
    f"_чтобы продолжить, выберите другой товар_\n"
)

PART_NOT_ENOUGH_AVAILABLE_COUNT_ERROR_TEXT = (
    f"\n⚠️ *произошла ошибка*\n"
    f"_выставлено максимально доступное количество товара, либо товар убран из корзины_\n"
)

INTO_CART_TEXT = (
    f"*[ 🛒 корзина ]*\n\n\n"
)

PARTS_PRESENTED_IN_CART_TEXT = (
    f"_ваши товары в корзине:_\n\n"
)

ORDER_CONFIRMATION_TEXT = (
    f"\n❔ *подтверждение заказа*. _вы уверены_?"
)

ORDER_CONFIRMATION_ERROR_TEXT = (
    f"\n⚠️ *произошла ошибка*\n"
    f"внимание, в корзине проведены изменения, продолжить?"
)

CONFIRMED_ORDERS_TEXT = (
    f"*[🕓 ваши заказы]*\n\n\n"
)

COMPLETED_ORDERS_TEXT = (
    f"*[✅ архив заказов]*\n\n\n"
)

CATEGORY_CHOICES = {
    "ABRSMATS": "🛠 абразивные материалы",
    "POLWHEEL": "🛠 полировальные круги",
    "PNTTAPES": "🛠 малярные ленты",
    "PLANES": "🛠 рубанки",
    "POLPASTS": "🛠 полировальные пасты",
    "SPRAYGUN": "🛠 краскопульты",
    "SUPPLIES": "🛠 расходные материалы",
    "OTHER": "🛠 другое"
}