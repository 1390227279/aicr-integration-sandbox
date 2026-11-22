from decimal import Decimal

FREE_SHIPPING_THRESHOLD = Decimal("99.00")
STANDARD_SHIPPING_FEE = Decimal("12.00")


def calculate_shipping_fee(order_subtotal: Decimal, is_vip: bool = False) -> Decimal:
    """Return the shipping fee for an order based on subtotal and VIP status."""
    if order_subtotal < Decimal("0.00"):
        raise ValueError("order_subtotal must be non-negative")
    if is_vip or order_subtotal >= FREE_SHIPPING_THRESHOLD:
        return Decimal("0.00")
    return STANDARD_SHIPPING_FEE
