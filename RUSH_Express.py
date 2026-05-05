import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class FoodDeliveryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("🍔 RUSH-Express 🍔")
        self.geometry("1100x700")
        self.minsize(1000, 650)
        
        self.cart = []
        self.user_name = "Foodies"
        self.orders_history = []
        self.currency = "₹"
        self.delivery_charge = 49
        
        self.menu_data = {
            "🍕 Pizza": [
                {"name": "Margherita Pizza", "price": 249, "desc": "Fresh tomatoes, mozzarella, basil", "emoji": "🍕"},
                {"name": "Pepperoni Pizza", "price": 349, "desc": "Classic pepperoni with cheese", "emoji": "🍕"},
                {"name": "BBQ Chicken Pizza", "price": 399, "desc": "BBQ sauce, chicken, red onions", "emoji": "🍕"},
                {"name": "Veggie Supreme", "price": 299, "desc": "Loaded with fresh vegetables", "emoji": "🍕"},
            ],
            "🍔 Burgers": [
                {"name": "Classic Cheeseburger", "price": 199, "desc": "Beef patty, cheese, lettuce, tomato", "emoji": "🍔"},
                {"name": "Bacon Deluxe", "price": 249, "desc": "Double bacon, cheese, special sauce", "emoji": "🍔"},
                {"name": "Veggie Burger", "price": 149, "desc": "Plant-based patty with veggies", "emoji": "🍔"},
                {"name": "Spicy Chicken", "price": 219, "desc": "Crispy spicy chicken fillet", "emoji": "🍔"},
            ],
            "🍣 Sushi": [
                {"name": "Salmon Roll", "price": 449, "desc": "Fresh salmon, avocado, rice", "emoji": "🍣"},
                {"name": "California Roll", "price": 379, "desc": "Crab, cucumber, avocado", "emoji": "🍣"},
                {"name": "Dragon Roll", "price": 549, "desc": "Eel, cucumber, avocado topping", "emoji": "🍣"},
                {"name": "Sushi Platter", "price": 799, "desc": "Mixed sushi selection", "emoji": "🍣"},
            ],
            "🥗 Salads": [
                {"name": "Caesar Salad", "price": 179, "desc": "Romaine, parmesan, croutons", "emoji": "🥗"},
                {"name": "Greek Salad", "price": 199, "desc": "Feta, olives, fresh vegetables", "emoji": "🥗"},
                {"name": "Quinoa Bowl", "price": 249, "desc": "Quinoa, avocado, mixed greens", "emoji": "🥗"},
            ],
            "🍰 Desserts": [
                {"name": "Chocolate Cake", "price": 149, "desc": "Rich chocolate layered cake", "emoji": "🍰"},
                {"name": "Cheesecake", "price": 179, "desc": "New York style cheesecake", "emoji": "🍰"},
                {"name": "Ice Cream Sundae", "price": 129, "desc": "Vanilla with chocolate sauce", "emoji": "🍨"},
                {"name": "Tiramisu", "price": 199, "desc": "Classic Italian dessert", "emoji": "🍰"},
            ],
            "🥤 Drinks": [
                {"name": "Coca Cola", "price": 60, "desc": "Classic refreshing soda", "emoji": "🥤"},
                {"name": "Fresh Orange Juice", "price": 120, "desc": "Freshly squeezed", "emoji": "🍊"},
                {"name": "Iced Coffee", "price": 99, "desc": "Cold brew coffee", "emoji": "☕"},
                {"name": "Smoothie", "price": 149, "desc": "Mixed berry smoothie", "emoji": "🥤"},
            ],
        }
        
        self.current_category = "🍕 Pizza"
        self.create_widgets()
    
    def create_widgets(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.create_sidebar()
        
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)
        
        self.create_header()
        self.create_category_bar()
        self.create_menu_area()
        self.create_cart_sidebar()
    
    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(7, weight=1)
        
        logo = ctk.CTkLabel(sidebar, text="🍔 RUSH-Express 🍔", 
                            font=ctk.CTkFont(size=22, weight="bold"))
        logo.grid(row=0, column=0, padx=20, pady=(30, 10))
        
        tagline = ctk.CTkLabel(sidebar, text="Fast & Delicious", 
                               font=ctk.CTkFont(size=12), text_color="gray")
        tagline.grid(row=1, column=0, padx=20, pady=(0, 30))
        
        nav_buttons = [
            ("🏠  Home", self.show_home),
            ("📋  Menu", self.show_home),
            ("🛒  My Cart", self.show_cart),
            ("📦  Orders", self.show_orders),
            ("👤  Profile", self.show_profile),
        ]
        
        for i, (text, command) in enumerate(nav_buttons, start=2):
            btn = ctk.CTkButton(sidebar, text=text, command=command,
                                anchor="w", height=45, corner_radius=10,
                                fg_color="transparent", text_color=("gray10", "gray90"),
                                hover_color=("gray70", "gray30"),
                                font=ctk.CTkFont(size=14))
            btn.grid(row=i, column=0, padx=15, pady=5, sticky="ew")
        
        theme_label = ctk.CTkLabel(sidebar, text="Appearance", 
                                    font=ctk.CTkFont(size=12), text_color="gray")
        theme_label.grid(row=8, column=0, padx=20, pady=(20, 5), sticky="w")
        
        theme_menu = ctk.CTkOptionMenu(sidebar, values=["Dark", "Light", "System"],
                                        command=self.change_theme, width=180)
        theme_menu.grid(row=9, column=0, padx=20, pady=(0, 20))
    
    def create_header(self):
        header = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        header.grid_columnconfigure(0, weight=1)
        
        welcome_frame = ctk.CTkFrame(header, fg_color="transparent")
        welcome_frame.grid(row=0, column=0, sticky="w")
        
        greeting = ctk.CTkLabel(welcome_frame, text=f"Hello, {self.user_name}! 👋",
                                font=ctk.CTkFont(size=24, weight="bold"))
        greeting.pack(anchor="w")
        
        subtitle = ctk.CTkLabel(welcome_frame, text="What would you like to eat today?",
                                font=ctk.CTkFont(size=14), text_color="gray")
        subtitle.pack(anchor="w")
        
        search_frame = ctk.CTkFrame(header, fg_color="transparent")
        search_frame.grid(row=0, column=1, sticky="e")
        
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="🔍 Search food...",
                                          width=250, height=40, corner_radius=20)
        self.search_entry.pack(side="left", padx=(0, 10))
        self.search_entry.bind("<KeyRelease>", lambda e: self.search_menu())
    
    def create_category_bar(self):
        cat_frame = ctk.CTkScrollableFrame(self.main_frame, height=60, 
                                            orientation="horizontal",
                                            fg_color="transparent")
        cat_frame.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        
        self.category_buttons = {}
        for i, category in enumerate(self.menu_data.keys()):
            is_active = category == self.current_category
            btn = ctk.CTkButton(cat_frame, text=category, height=40, width=120,
                                corner_radius=20,
                                fg_color=("#1f6aa5" if is_active else "transparent"),
                                text_color=("white" if is_active else ("gray10", "gray90")),
                                hover_color=("#144870"),
                                border_width=0 if is_active else 1,
                                border_color="gray",
                                font=ctk.CTkFont(size=13, weight="bold"),
                                command=lambda c=category: self.change_category(c))
            btn.grid(row=0, column=i, padx=5, pady=5)
            self.category_buttons[category] = btn
    
    def create_menu_area(self):
        self.menu_scroll = ctk.CTkScrollableFrame(self.main_frame, fg_color="transparent")
        self.menu_scroll.grid(row=2, column=0, sticky="nsew")
        self.menu_scroll.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.display_menu_items()
    
    def display_menu_items(self, search_term=""):
        for widget in self.menu_scroll.winfo_children():
            widget.destroy()
        
        items = self.menu_data[self.current_category]
        if search_term:
            items = [item for item in items if search_term.lower() in item["name"].lower()]
        
        if not items:
            no_results = ctk.CTkLabel(self.menu_scroll, text="No items found 😔",
                                       font=ctk.CTkFont(size=16))
            no_results.grid(row=0, column=0, columnspan=3, pady=50)
            return
        
        for i, item in enumerate(items):
            row = i // 3
            col = i % 3
            self.create_food_card(self.menu_scroll, item, row, col)
    
    def create_food_card(self, parent, item, row, col):
        card = ctk.CTkFrame(parent, corner_radius=15, height=220)
        card.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
        card.grid_propagate(False)
        
        emoji_label = ctk.CTkLabel(card, text=item["emoji"], font=ctk.CTkFont(size=50))
        emoji_label.pack(pady=(15, 5))
        
        name_label = ctk.CTkLabel(card, text=item["name"], 
                                   font=ctk.CTkFont(size=15, weight="bold"))
        name_label.pack(pady=(0, 5))
        
        desc_label = ctk.CTkLabel(card, text=item["desc"], 
                                   font=ctk.CTkFont(size=11),
                                   text_color="gray", wraplength=200)
        desc_label.pack(pady=(0, 10))
        
        bottom_frame = ctk.CTkFrame(card, fg_color="transparent")
        bottom_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        price_label = ctk.CTkLabel(bottom_frame, text=f"₹{item['price']:.2f}",
                                    font=ctk.CTkFont(size=16, weight="bold"),
                                    text_color="#1f6aa5")
        price_label.pack(side="left")
        
        add_btn = ctk.CTkButton(bottom_frame, text="+ Add", width=70, height=30,
                                 corner_radius=15,
                                 font=ctk.CTkFont(size=12, weight="bold"),
                                 command=lambda: self.add_to_cart(item))
        add_btn.pack(side="right")
    
    def create_cart_sidebar(self):
        self.cart_frame = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.cart_frame.grid(row=0, column=2, sticky="nsew")
        self.cart_frame.grid_rowconfigure(1, weight=1)
        self.cart_frame.grid_propagate(False)
        
        cart_header = ctk.CTkFrame(self.cart_frame, fg_color="transparent")
        cart_header.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        
        cart_title = ctk.CTkLabel(cart_header, text="🛒 Your Cart",
                                   font=ctk.CTkFont(size=20, weight="bold"))
        cart_title.pack(anchor="w")
        
        self.cart_count = ctk.CTkLabel(cart_header, text="0 items",
                                        font=ctk.CTkFont(size=12), text_color="gray")
        self.cart_count.pack(anchor="w")
        
        self.cart_items_frame = ctk.CTkScrollableFrame(self.cart_frame, fg_color="transparent")
        self.cart_items_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=5)
        
        self.cart_footer = ctk.CTkFrame(self.cart_frame, corner_radius=0)
        self.cart_footer.grid(row=2, column=0, sticky="ew")
        
        self.update_cart_display()
    
    def update_cart_display(self):
        for widget in self.cart_items_frame.winfo_children():
            widget.destroy()
        for widget in self.cart_footer.winfo_children():
            widget.destroy()
        
        self.cart_count.configure(text=f"{len(self.cart)} items")
        
        if not self.cart:
            empty_label = ctk.CTkLabel(self.cart_items_frame, 
                                        text="🛒\n\nYour cart is empty\nAdd some delicious food!",
                                        font=ctk.CTkFont(size=13),
                                        text_color="gray", justify="center")
            empty_label.pack(pady=50)
            return
        
        grouped = {}
        for item in self.cart:
            key = item["name"]
            if key in grouped:
                grouped[key]["qty"] += 1
            else:
                grouped[key] = {"item": item, "qty": 1}
        
        for name, data in grouped.items():
            item = data["item"]
            qty = data["qty"]
            
            item_frame = ctk.CTkFrame(self.cart_items_frame, corner_radius=10)
            item_frame.pack(fill="x", pady=5)
            
            top_row = ctk.CTkFrame(item_frame, fg_color="transparent")
            top_row.pack(fill="x", padx=10, pady=(10, 5))
            
            emoji_lbl = ctk.CTkLabel(top_row, text=item["emoji"], 
                                      font=ctk.CTkFont(size=24))
            emoji_lbl.pack(side="left")
            
            info_frame = ctk.CTkFrame(top_row, fg_color="transparent")
            info_frame.pack(side="left", fill="x", expand=True, padx=10)
            
            name_lbl = ctk.CTkLabel(info_frame, text=item["name"],
                                     font=ctk.CTkFont(size=12, weight="bold"),
                                     anchor="w")
            name_lbl.pack(anchor="w")
            
            price_lbl = ctk.CTkLabel(info_frame, 
                                      text=f"₹{item['price'] * qty:.2f}",
                                      font=ctk.CTkFont(size=11),
                                      text_color="#1f6aa5", anchor="w")
            price_lbl.pack(anchor="w")
            
            qty_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
            qty_frame.pack(fill="x", padx=10, pady=(0, 10))
            
            minus_btn = ctk.CTkButton(qty_frame, text="−", width=25, height=25,
                                       corner_radius=12,
                                       command=lambda i=item: self.remove_from_cart(i))
            minus_btn.pack(side="left")
            
            qty_lbl = ctk.CTkLabel(qty_frame, text=str(qty), width=30,
                                    font=ctk.CTkFont(size=12, weight="bold"))
            qty_lbl.pack(side="left", padx=5)
            
            plus_btn = ctk.CTkButton(qty_frame, text="+", width=25, height=25,
                                      corner_radius=12,
                                      command=lambda i=item: self.add_to_cart(i, silent=True))
            plus_btn.pack(side="left")
        
        subtotal = sum(item["price"] for item in self.cart)
        delivery = self.delivery_charge if subtotal > 0 else 0
        total = subtotal + delivery
        
        ctk.CTkLabel(self.cart_footer, text="").pack(pady=5)
        
        sub_frame = ctk.CTkFrame(self.cart_footer, fg_color="transparent")
        sub_frame.pack(fill="x", padx=20, pady=2)
        ctk.CTkLabel(sub_frame, text="Subtotal", text_color="gray",
                     font=ctk.CTkFont(size=12)).pack(side="left")
        ctk.CTkLabel(sub_frame, text=f"₹{subtotal:.2f}",
                     font=ctk.CTkFont(size=12)).pack(side="right")
        
        del_frame = ctk.CTkFrame(self.cart_footer, fg_color="transparent")
        del_frame.pack(fill="x", padx=20, pady=2)
        ctk.CTkLabel(del_frame, text="Delivery", text_color="gray",
                     font=ctk.CTkFont(size=12)).pack(side="left")
        ctk.CTkLabel(del_frame, text=f"₹{delivery:.2f}",
                     font=ctk.CTkFont(size=12)).pack(side="right")
        
        sep = ctk.CTkFrame(self.cart_footer, height=1, fg_color="gray")
        sep.pack(fill="x", padx=20, pady=8)
        
        total_frame = ctk.CTkFrame(self.cart_footer, fg_color="transparent")
        total_frame.pack(fill="x", padx=20, pady=2)
        ctk.CTkLabel(total_frame, text="Total",
                     font=ctk.CTkFont(size=15, weight="bold")).pack(side="left")
        ctk.CTkLabel(total_frame, text=f"₹{total:.2f}",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color="#1f6aa5").pack(side="right")
        
        checkout_btn = ctk.CTkButton(self.cart_footer, text="Checkout 🚀",
                                      height=45, corner_radius=15,
                                      font=ctk.CTkFont(size=14, weight="bold"),
                                      command=self.checkout)
        checkout_btn.pack(fill="x", padx=20, pady=15)
    
    def add_to_cart(self, item, silent=False):
        self.cart.append(item)
        self.update_cart_display()
        if not silent:
            self.show_toast(f"✅ {item['name']} added to cart!")
    
    def remove_from_cart(self, item):
        for i, cart_item in enumerate(self.cart):
            if cart_item["name"] == item["name"]:
                self.cart.pop(i)
                break
        self.update_cart_display()
    
    def show_toast(self, message):
        toast = ctk.CTkToplevel(self)
        toast.geometry("300x50")
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)
        
        x = self.winfo_x() + (self.winfo_width() // 2) - 150
        y = self.winfo_y() + 100
        toast.geometry(f"300x50+{x}+{y}")
        
        label = ctk.CTkLabel(toast, text=message, 
                              font=ctk.CTkFont(size=13, weight="bold"),
                              fg_color="#1f6aa5", corner_radius=10,
                              text_color="white")
        label.pack(fill="both", expand=True, padx=5, pady=5)
        
        toast.after(1500, toast.destroy)
    
    def change_category(self, category):
        self.current_category = category
        for cat, btn in self.category_buttons.items():
            if cat == category:
                btn.configure(fg_color="#1f6aa5", text_color="white", border_width=0)
            else:
                btn.configure(fg_color="transparent", 
                              text_color=("gray10", "gray90"), border_width=1)
        self.display_menu_items()
    
    def search_menu(self):
        term = self.search_entry.get()
        self.display_menu_items(term)
    
    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Please add items to your cart first!")
            return
        
        checkout_win = ctk.CTkToplevel(self)
        checkout_win.title("Checkout")
        checkout_win.geometry("450x550")
        checkout_win.transient(self)
        checkout_win.grab_set()
        
        ctk.CTkLabel(checkout_win, text="🚀 Checkout",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        
        form = ctk.CTkFrame(checkout_win, fg_color="transparent")
        form.pack(fill="x", padx=30, pady=10)
        
        ctk.CTkLabel(form, text="Full Name", anchor="w",
                     font=ctk.CTkFont(size=12)).pack(fill="x")
        name_entry = ctk.CTkEntry(form, height=40, placeholder_text="Rahul Sharma")
        name_entry.pack(fill="x", pady=(5, 15))
        
        ctk.CTkLabel(form, text="Delivery Address", anchor="w",
                     font=ctk.CTkFont(size=12)).pack(fill="x")
        addr_entry = ctk.CTkEntry(form, height=40, placeholder_text="123 MG Road, Mumbai")
        addr_entry.pack(fill="x", pady=(5, 15))
        
        ctk.CTkLabel(form, text="Phone Number", anchor="w",
                     font=ctk.CTkFont(size=12)).pack(fill="x")
        phone_entry = ctk.CTkEntry(form, height=40, placeholder_text="+91 98765 43210")
        phone_entry.pack(fill="x", pady=(5, 15))
        
        ctk.CTkLabel(form, text="Payment Method", anchor="w",
                     font=ctk.CTkFont(size=12)).pack(fill="x")
        payment = ctk.CTkOptionMenu(form, values=["💳 Credit/Debit Card", "💵 Cash on Delivery", "📱 UPI / PhonePe / GPay"],
                                     height=40)
        payment.pack(fill="x", pady=(5, 15))
        
        subtotal = sum(item["price"] for item in self.cart)
        total = subtotal + self.delivery_charge
        
        total_lbl = ctk.CTkLabel(checkout_win, text=f"Total: ₹{total:.2f}",
                                  font=ctk.CTkFont(size=20, weight="bold"),
                                  text_color="#1f6aa5")
        total_lbl.pack(pady=10)
        
        def place_order():
            if not name_entry.get() or not addr_entry.get() or not phone_entry.get():
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            order_id = f"#{random.randint(10000, 99999)}"
            order = {
                "id": order_id,
                "items": list(self.cart),
                "total": total,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "status": "Preparing"
            }
            self.orders_history.append(order)
            self.user_name = name_entry.get().split()[0]
            
            messagebox.showinfo("Order Placed! 🎉", 
                                f"Your order {order_id} has been placed!\n\n"
                                f"Estimated delivery: 30-45 minutes\n"
                                f"Total: ₹{total:.2f}\n\n"
                                f"Thank you for ordering with us!")
            
            self.cart.clear()
            self.update_cart_display()
            checkout_win.destroy()
        
        ctk.CTkButton(checkout_win, text="Place Order 🎉", height=45,
                      corner_radius=15,
                      font=ctk.CTkFont(size=14, weight="bold"),
                      command=place_order).pack(fill="x", padx=30, pady=20)
    
    def show_home(self):
        pass
    
    def show_cart(self):
        if not self.cart:
            messagebox.showinfo("Cart", "Your cart is empty!")
        else:
            self.show_toast(f"You have {len(self.cart)} items in your cart")
    
    def show_orders(self):
        orders_win = ctk.CTkToplevel(self)
        orders_win.title("My Orders")
        orders_win.geometry("500x600")
        orders_win.transient(self)
        
        ctk.CTkLabel(orders_win, text="📦 Order History",
                     font=ctk.CTkFont(size=22, weight="bold")).pack(pady=20)
        
        if not self.orders_history:
            ctk.CTkLabel(orders_win, text="No orders yet 😔\nStart ordering now!",
                         font=ctk.CTkFont(size=14), text_color="gray").pack(pady=50)
            return
        
        scroll = ctk.CTkScrollableFrame(orders_win)
        scroll.pack(fill="both", expand=True, padx=20, pady=10)
        
        for order in reversed(self.orders_history):
            order_card = ctk.CTkFrame(scroll, corner_radius=10)
            order_card.pack(fill="x", pady=5)
            
            header = ctk.CTkFrame(order_card, fg_color="transparent")
            header.pack(fill="x", padx=15, pady=10)
            
            ctk.CTkLabel(header, text=f"Order {order['id']}",
                         font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
            ctk.CTkLabel(header, text=order["status"],
                         font=ctk.CTkFont(size=11),
                         text_color="#1f6aa5").pack(side="right")
            
            ctk.CTkLabel(order_card, text=f"📅 {order['date']}",
                         font=ctk.CTkFont(size=11),
                         text_color="gray").pack(anchor="w", padx=15)
            ctk.CTkLabel(order_card, text=f"🍽️ {len(order['items'])} items",
                         font=ctk.CTkFont(size=11),
                         text_color="gray").pack(anchor="w", padx=15)
            ctk.CTkLabel(order_card, text=f"💰 ₹{order['total']:.2f}",
                         font=ctk.CTkFont(size=13, weight="bold"),
                         text_color="#1f6aa5").pack(anchor="w", padx=15, pady=(5, 10))
    
    def show_profile(self):
        messagebox.showinfo("Profile", f"User: {self.user_name}\n"
                            f"Total Orders: {len(self.orders_history)}\n"
                            f"Member since: 2024")
    
    def change_theme(self, mode):
        ctk.set_appearance_mode(mode.lower())


if __name__ == "__main__":
    app = FoodDeliveryApp()
    app.mainloop()
