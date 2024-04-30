
# /api/orders           - Customer      - GET  - Returns all orders with order items created by this user

# /api/orders           - Customer      - POST - Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.

# /api/orders/{orderId} - Customer      - GET  - Returns all items for this order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.

# /api/orders           - Manager       - GET - Returns all orders with order items by all users

# /api/orders/{orderId} - Customer      - PUT, PATCH -
# Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1.
# If a delivery crew is assigned to this order and the status = 0, it means the order is out for delivery.
# If a delivery crew is assigned to this order and the status = 1, it means the order has been delivered.

# /api/orders/{orderId} - Manager       - DELETE - Deletes this order

# /api/orders           - Delivery crew - GET    - Returns all orders with order items assigned to the delivery crew

# /api/orders/{orderId} - Delivery crew - PATCH  - A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.