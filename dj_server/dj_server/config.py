import datetime

TZ_OFFSET = datetime.timedelta(hours=3)

TIMESTAMP_START = datetime.datetime.now()

TITLE = 'MalarkaShop'
CHANNEL_LINK="tg://resolve?domain=malarkashop_bot"


"""CHOICES FOR CERTAIN PARTS CATEGORY"""

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


"""
    TEXT PLACEOLDERS
    START
"""

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
    f"введите количество товара, которое хотите добавить в корзину\n\n"
    f"*0* - _удалить из корзины_"
)

ENTER_USER_NAME_TEXT = (
    f"как к вам обращаться? (макс. 32 симв.)"
)

ENTER_USER_PHONE_NUMBER_TEXT = (
    f"ваш телефон?\n"
    f"в следующем формате: _(25, 29, 33, 44)xxxxxxx_"
    f"(9 цифр после +375)"
)

ENTER_USER_DELIVERY_ADDRESS_TEXT = (
    f"адрес доставки? (макс. 128 симв.)"
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

ALL_CONFIRMED_ORDERS_TEXT = (
    f"*[🕓 выполняемые заказы]*\n\n\n"
)

COMPLETED_ORDERS_TEXT = (
    f"*[✅ архив заказов]*\n\n\n"
)

"""
    TEXT PLACEOLDERS
    END
"""