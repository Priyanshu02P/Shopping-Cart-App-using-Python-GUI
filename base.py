import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
import csv
from datetime import datetime
from const import *

class EcommerceApp:
    def __init__(self, root, creds, product, discount_codes):
        self.root = root
        self.root.title("E-commerce Application")
        self.root.geometry("1200x700")
        self.root.resizable(True, True)
        
        self.setup_data(creds, product)
        self.current_user = None
        self.discount_codes = discount_codes
        self.applied_discount = 0
        self.create_login_screen()
    
    def setup_data(self, creds, product):
        """Initialize data from credentials and products"""
        self.db = pd.DataFrame(creds, columns=["ID", "Password"])
        self.productsDB = pd.DataFrame(product, columns=["ProductID", "ProductName", "Category", "Price"])
        self.billDB = pd.DataFrame(columns=["ProductID", "ProductName", "Category", "Price", "Quantity"])
        self.categories = ["All"] + sorted(self.productsDB["Category"].unique().tolist())

    def checkLogin(self, DataBase, ID, PassWord):
        check = DataBase.loc[DataBase["ID"] == ID]
        if check.empty:
            return False
        if check.iloc[0]["Password"] == PassWord:
            return True
        else:
            return False

    def signIn(self, DataBase, Creds):
        if (DataBase.loc[DataBase["ID"] == Creds["ID"]]).empty:
            DataBase = pd.concat([DataBase, pd.DataFrame(Creds, index=[0])], ignore_index=True)
            Check = True
        else:
            Check = False
        return DataBase, Check

    def randomShuffle(self, DataBase):
        return DataBase.sample(frac=1).reset_index(drop=True)

    def sortByCategory(self, DataBase, Category):
        if Category == "All":
            return DataBase
        return DataBase.loc[DataBase["Category"] == Category]

    def sortByPrice(self, DataBase):
        return DataBase.sort_values(by="Price")

    def getByID(self, DataBase, ID):
        return DataBase.loc[DataBase["ProductID"] == ID]

    def addToBill(self, Bill, Product):
        qty = self.getByID(Bill, int(Product["ProductID"]))
        if qty.empty:
            Product = Product.copy()
            Product.loc[Product.index[0], "Quantity"] = 1
            Bill = pd.concat([Bill, Product], ignore_index=True)
        else:
            Bill.loc[Bill["ProductID"] == Product["ProductID"].iloc[0], "Quantity"] += 1
        return Bill

    def removeFromBill(self, Bill, Product):
        qty = self.getByID(Bill, int(Product["ProductID"]))
        if not qty.empty:
            if qty.iloc[0]["Quantity"] > 1:
                Bill.loc[Bill["ProductID"] == Product["ProductID"].iloc[0], "Quantity"] -= 1
            else:
                Bill = Bill[Bill["ProductID"] != Product["ProductID"].iloc[0]].reset_index(drop=True)
        return Bill

    def create_login_screen(self):
        """Create the login interface"""
        self.clear_screen()
        
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True)
        
        login_frame = tk.Frame(main_frame, bg='white', padx=40, pady=40, relief='raised', bd=2)
        login_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        title_label = tk.Label(login_frame, text="E-commerce Login", font=('Arial', 24, 'bold'), bg='white', fg='#333')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        id_label = tk.Label(login_frame, text="User ID:", font=('Arial', 12), bg='white')
        id_label.grid(row=1, column=0, sticky='e', padx=(0, 10), pady=10)
        
        self.id_entry = tk.Entry(login_frame, font=('Arial', 12), width=20)
        self.id_entry.grid(row=1, column=1, pady=10)
        
        pass_label = tk.Label(login_frame, text="Password:", font=('Arial', 12), bg='white')
        pass_label.grid(row=2, column=0, sticky='e', padx=(0, 10), pady=10)
        
        self.pass_entry = tk.Entry(login_frame, font=('Arial', 12), width=20, show='*')
        self.pass_entry.grid(row=2, column=1, pady=10)
        
        login_btn = tk.Button(login_frame, text="Login", font=('Arial', 12), 
                             bg='#4CAF50', fg='white', command=self.login, width=10)
        login_btn.grid(row=3, column=0, pady=20, padx=5)
        
        signup_btn = tk.Button(login_frame, text="Sign Up", font=('Arial', 12), 
                              bg='#2196F3', fg='white', command=self.show_signup, width=10)
        signup_btn.grid(row=3, column=1, pady=20, padx=5)
        
        info_label = tk.Label(login_frame, text="Sample: ID: 24AIML043, Password: 8888", 
                             font=('Arial', 10), bg='white', fg='#666')
        info_label.grid(row=4, column=0, columnspan=2, pady=10)

    def show_signup(self):
        """Show signup dialog window"""
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")
        signup_window.geometry("400x300")
        signup_window.transient(self.root)
        signup_window.grab_set()
        
        signup_window.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        frame = tk.Frame(signup_window, padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="Create New Account", font=('Arial', 16, 'bold')).pack(pady=10)
        
        tk.Label(frame, text="User ID:").pack()
        id_entry = tk.Entry(frame, width=30)
        id_entry.pack(pady=5)
        
        tk.Label(frame, text="Password:").pack()
        pass_entry = tk.Entry(frame, width=30, show='*')
        pass_entry.pack(pady=5)
        
        tk.Label(frame, text="Confirm Password:").pack()
        confirm_entry = tk.Entry(frame, width=30, show='*')
        confirm_entry.pack(pady=5)
        
        def create_account():
            user_id = id_entry.get().strip()
            password = pass_entry.get()
            confirm = confirm_entry.get()
            
            if not user_id or not password:
                messagebox.showerror("Error", "Please fill all fields")
                return
                
            if password != confirm:
                messagebox.showerror("Error", "Passwords don't match")
                return
                
            creds = {"ID": user_id, "Password": password}
            self.db, success = self.signIn(self.db, creds)
            
            if success:
                messagebox.showinfo("Success", "Account created successfully!")
                signup_window.destroy()
            else:
                messagebox.showerror("Error", "User ID already exists")
        
        tk.Button(frame, text="Create Account", command=create_account, 
                 bg='#4CAF50', fg='white', width=15).pack(pady=20)

    def login(self):
        """Handle user login validation"""
        user_id = self.id_entry.get().strip()
        password = self.pass_entry.get()
        
        if not user_id or not password:
            messagebox.showerror("Error", "Please enter both ID and password")
            return
            
        if self.checkLogin(self.db, user_id, password):
            self.current_user = user_id
            self.create_main_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def create_main_screen(self):
        """Create the main shopping interface"""
        self.clear_screen()
        
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        top_frame = tk.Frame(main_frame, bg='#2196F3', height=60)
        top_frame.pack(fill='x', pady=(0, 10))
        top_frame.pack_propagate(False)
        
        welcome_label = tk.Label(top_frame, text=f"Welcome, {self.current_user}!", 
                                font=('Arial', 14, 'bold'), bg='#2196F3', fg='white')
        welcome_label.pack(side='left', padx=20, pady=15)
        
        logout_btn = tk.Button(top_frame, text="Logout", command=self.logout, 
                              bg='#f44336', fg='white', font=('Arial', 10))
        logout_btn.pack(side='right', padx=20, pady=15)
        
        content_frame = tk.Frame(main_frame)
        content_frame.pack(fill='both', expand=True)
        
        left_frame = tk.Frame(content_frame, bg='#f5f5f5', relief='raised', bd=1)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        products_header = tk.Frame(left_frame, bg='#f5f5f5')
        products_header.pack(fill='x', padx=10, pady=10)
        
        tk.Label(products_header, text="Products", font=('Arial', 16, 'bold'), bg='#f5f5f5').pack(side='left')
        
        controls_frame = tk.Frame(products_header, bg='#f5f5f5')
        controls_frame.pack(side='right')
        
        tk.Button(controls_frame, text="Sort by Price", command=self.sort_by_price, 
                 bg='#FF9800', fg='white', font=('Arial', 9)).pack(side='right', padx=2)
        
        tk.Label(controls_frame, text="Category:", bg='#f5f5f5', font=('Arial', 10)).pack(side='right', padx=5)
        self.category_var = tk.StringVar(value="All")
        category_menu = ttk.Combobox(controls_frame, textvariable=self.category_var, 
                                   values=self.categories, state='readonly', width=15)
        category_menu.pack(side='right', padx=2)
        category_menu.bind('<<ComboboxSelected>>', self.filter_by_category)
        
        products_container = tk.Frame(left_frame)
        products_container.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        self.products_canvas = tk.Canvas(products_container, bg='white')
        products_scrollbar = ttk.Scrollbar(products_container, orient="vertical", command=self.products_canvas.yview)
        self.products_scrollable_frame = tk.Frame(self.products_canvas, bg='white')
        
        self.products_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.products_canvas.configure(scrollregion=self.products_canvas.bbox("all"))
        )
        
        self.products_canvas.create_window((0, 0), window=self.products_scrollable_frame, anchor="nw")
        self.products_canvas.configure(yscrollcommand=products_scrollbar.set)
        
        self.products_canvas.pack(side="left", fill="both", expand=True)
        products_scrollbar.pack(side="right", fill="y")
        
        right_frame = tk.Frame(content_frame, bg='#e8f5e8', relief='raised', bd=1, width=350)
        right_frame.pack(side='right', fill='y', padx=(5, 0))
        right_frame.pack_propagate(False)
        
        cart_header = tk.Frame(right_frame, bg='#4CAF50')
        cart_header.pack(fill='x')
        
        tk.Label(cart_header, text="Shopping Cart", font=('Arial', 14, 'bold'), 
                bg='#4CAF50', fg='white').pack(pady=10)
        
        cart_container = tk.Frame(right_frame)
        cart_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.cart_canvas = tk.Canvas(cart_container, bg='white', width=320)
        cart_scrollbar = ttk.Scrollbar(cart_container, orient="vertical", command=self.cart_canvas.yview)
        self.cart_scrollable_frame = tk.Frame(self.cart_canvas, bg='white', width=320)
        
        def on_cart_configure(event):
            self.cart_canvas.configure(scrollregion=self.cart_canvas.bbox("all"))
        
        self.cart_scrollable_frame.bind("<Configure>", on_cart_configure)
        
        self.cart_window = self.cart_canvas.create_window((0, 0), window=self.cart_scrollable_frame, anchor="nw")
        self.cart_canvas.configure(yscrollcommand=cart_scrollbar.set)
        
        # Force the canvas window to match our fixed width
        self.cart_canvas.itemconfig(self.cart_window, width=320)
        
        self.cart_canvas.pack(side="left", fill="both", expand=True)
        cart_scrollbar.pack(side="right", fill="y")
        
        cart_footer = tk.Frame(right_frame, bg='#e8f5e8')
        cart_footer.pack(fill='x', padx=10, pady=10)
        
        discount_frame = tk.Frame(cart_footer, bg='#e8f5e8')
        discount_frame.pack(fill='x', pady=5)
        
        tk.Label(discount_frame, text="Discount Code:", bg='#e8f5e8', font=('Arial', 10)).pack()
        self.discount_entry = tk.Entry(discount_frame, width=15)
        self.discount_entry.pack(pady=2)
        tk.Button(discount_frame, text="Apply", command=self.apply_discount, 
                 bg='#FF5722', fg='white', font=('Arial', 9)).pack(pady=2)
        
        self.total_label = tk.Label(cart_footer, text="Total: $0.00", font=('Arial', 12, 'bold'), bg='#e8f5e8')
        self.total_label.pack(pady=5)
        
        tk.Button(cart_footer, text="Save Bill", command=self.save_bill, 
                 bg='#9C27B0', fg='white', width=15).pack(pady=2)
        tk.Button(cart_footer, text="Clear Cart", command=self.clear_cart, 
                 bg='#f44336', fg='white', width=15).pack(pady=2)
        
        self.current_products = self.productsDB.copy()
        self.update_products_display()
        self.update_cart_display()

    def clear_screen(self):
        """Clear all widgets from the screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def logout(self):
        """Handle user logout and reset session"""
        self.current_user = None
        self.billDB = pd.DataFrame(columns=["ProductID", "ProductName", "Category", "Price", "Quantity"])
        self.applied_discount = 0
        self.create_login_screen()

    def sort_by_price(self):
        self.current_products = self.sortByPrice(self.current_products)
        self.update_products_display()

    def filter_by_category(self, event=None):
        category = self.category_var.get()
        self.current_products = self.sortByCategory(self.productsDB, category)
        self.update_products_display()

    def update_products_display(self):
        """Update the products display with consistent layout and proper scrolling"""
        for widget in self.products_scrollable_frame.winfo_children():
            widget.destroy()

        self.main_container = tk.Frame(self.products_scrollable_frame, bg='white')
        self.main_container.pack(fill='both', expand=True, padx=5, pady=5)

        cols = 2
        
        for col in range(cols):
            self.main_container.columnconfigure(col, weight=1, uniform="products")

        def configure_canvas_width(event):
            canvas_width = event.width - 20
            if self.products_canvas.find_all():
                self.products_canvas.itemconfig(self.products_canvas.find_all()[0], width=canvas_width)

        # Enable mousewheel scrolling for products
        def on_mousewheel_products(event):
            self.products_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def bind_mousewheel_products(event):
            self.products_canvas.bind_all("<MouseWheel>", on_mousewheel_products)
        
        def unbind_mousewheel_products(event):
            self.products_canvas.unbind_all("<MouseWheel>")
        
        self.products_canvas.bind('<Configure>', configure_canvas_width)
        self.products_canvas.bind('<Enter>', bind_mousewheel_products)
        self.products_canvas.bind('<Leave>', unbind_mousewheel_products)
        
        self.recreate_products_grid(self.main_container, cols)

    def recreate_products_grid(self, container, cols):
        """Create products grid with specified column count"""
        for widget in container.winfo_children():
            widget.destroy()
            
        for idx, (_, product) in enumerate(self.current_products.iterrows()):
            row = idx // cols
            col = idx % cols
            
            product_frame = tk.Frame(container, bg='white', relief='ridge', bd=2)
            product_frame.grid(row=row, column=col, sticky='nsew', padx=3, pady=3)
            
            container.rowconfigure(row, weight=1)
            
            inner_frame = tk.Frame(product_frame, bg='white')
            inner_frame.pack(fill='both', expand=True, padx=8, pady=8)
            
            info_frame = tk.Frame(inner_frame, bg='white')
            info_frame.pack(fill='x', pady=(0, 8))
            
            name_label = tk.Label(info_frame, text=product['ProductName'], font=('Arial', 11, 'bold'), 
                                bg='white', anchor='w', wraplength=240, justify='left')
            name_label.pack(fill='x', pady=1)
            
            category_label = tk.Label(info_frame, text=f"Category: {product['Category']}", 
                                    font=('Arial', 9), bg='white', fg='#666', anchor='w')
            category_label.pack(fill='x', pady=1)
            
            id_label = tk.Label(info_frame, text=f"ID: {product['ProductID']}", 
                              font=('Arial', 8), bg='white', fg='#888', anchor='w')
            id_label.pack(fill='x', pady=1)
            
            bottom_frame = tk.Frame(inner_frame, bg='white')
            bottom_frame.pack(fill='x', side='bottom')
            
            price_frame = tk.Frame(bottom_frame, bg='white')
            price_frame.pack(side='left', fill='x', expand=True)
            
            price_label = tk.Label(price_frame, text=f"${product['Price']:.2f}", 
                                 font=('Arial', 12, 'bold'), bg='white', fg='#4CAF50', anchor='w')
            price_label.pack(side='left')
            
            add_btn = tk.Button(bottom_frame, text="Add to Cart", font=('Arial', 9, 'bold'), 
                              bg='#4CAF50', fg='white', 
                              command=lambda p=product: self.add_to_cart(p))
            add_btn.pack(side='right')

    def add_to_cart(self, product):
        product_df = pd.DataFrame([product])
        self.billDB = self.addToBill(self.billDB, product_df)
        self.update_cart_display()

    def remove_from_cart(self, product):
        product_df = pd.DataFrame([product])
        self.billDB = self.removeFromBill(self.billDB, product_df)
        self.update_cart_display()

    def update_cart_display(self):
        """Update the cart display """
        for widget in self.cart_scrollable_frame.winfo_children():
            widget.destroy()
            
        def configure_cart_width(event):
            canvas_width = event.width - 20
            if self.cart_canvas.find_all():
                self.cart_canvas.itemconfig(self.cart_canvas.find_all()[0], width=canvas_width)
        
        self.cart_canvas.bind('<Configure>', configure_cart_width)
        
        # Enable mousewheel scrolling for cart
        def on_mousewheel(event):
            self.cart_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def bind_mousewheel(event):
            self.cart_canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        def unbind_mousewheel(event):
            self.cart_canvas.unbind_all("<MouseWheel>")
        
        self.cart_canvas.bind('<Enter>', bind_mousewheel)
        self.cart_canvas.bind('<Leave>', unbind_mousewheel)
            
        if self.billDB.empty:
            empty_frame = tk.Frame(self.cart_scrollable_frame, bg='white')
            empty_frame.pack(fill='both', expand=True)
            
            tk.Label(empty_frame, text="Cart is empty", 
                    font=('Arial', 12), bg='white', fg='#666').pack(expand=True)
        else:
            for _, item in self.billDB.iterrows():
                item_frame = tk.Frame(self.cart_scrollable_frame, bg='white', relief='ridge', bd=1)
                item_frame.pack(fill='x', padx=1, pady=2, expand=True)
                
                inner_container = tk.Frame(item_frame, bg='white')
                inner_container.pack(fill='x', padx=1, pady=2, expand=True)
                
                # Product name 
                name_label = tk.Label(inner_container, text=item['ProductName'], 
                                    font=('Arial', 10, 'bold'), bg='white', anchor='w',
                                    wraplength=280, justify='left')
                name_label.pack(fill='x', pady=(0, 6))
                
                # Bottom section with price and controls
                bottom_frame = tk.Frame(inner_container, bg='white')
                bottom_frame.pack(fill='x')
                
                # Left: Price information (takes most space)
                price_frame = tk.Frame(bottom_frame, bg='white')
                price_frame.pack(side='left', fill='x', expand=True)
                
                unit_price_text = f"${item['Price']:.2f} each"
                unit_price_label = tk.Label(price_frame, text=unit_price_text, 
                                          font=('Arial', 9), bg='white', fg='#666', anchor='w')
                unit_price_label.pack(anchor='w')
                
                total_price_text = f"Total: ${item['Price'] * item['Quantity']:.2f}"
                total_price_label = tk.Label(price_frame, text=total_price_text, 
                                           font=('Arial', 9, 'bold'), bg='white', fg='#4CAF50', anchor='w')
                total_price_label.pack(anchor='w')
                
                # Right: Quantity controls (compact)
                controls_frame = tk.Frame(bottom_frame, bg='white')
                controls_frame.pack(side='right', padx=(10, 0))
                
                # Quantity label above controls
                qty_info_label = tk.Label(controls_frame, text="Qty:", 
                                        font=('Arial', 8), bg='white', fg='#666')
                qty_info_label.pack()
                
                # Controls row
                controls_row = tk.Frame(controls_frame, bg='white')
                controls_row.pack()
                
                remove_btn = tk.Button(controls_row, text="-", font=('Arial', 10, 'bold'), 
                                     bg='#f44336', fg='white', width=2, height=1,
                                     command=lambda i=item: self.remove_from_cart(i))
                remove_btn.pack(side='left')
                
                qty_label = tk.Label(controls_row, text=str(int(item['Quantity'])), 
                                   font=('Arial', 10, 'bold'), bg='#f0f0f0', width=3, height=1,
                                   relief='sunken', bd=1)
                qty_label.pack(side='left', padx=2)
                
                add_btn = tk.Button(controls_row, text="+", font=('Arial', 10, 'bold'), 
                                  bg='#4CAF50', fg='white', width=2, height=1,
                                  command=lambda i=item: self.add_to_cart(i))
                add_btn.pack(side='right')
        
        self.update_total()
        
        # Update scroll region after all widgets are added
        self.root.after(10, lambda: self.cart_canvas.configure(scrollregion=self.cart_canvas.bbox("all")))
        self.root.after(20, lambda: self.cart_canvas.event_generate('<Configure>'))

    def update_total(self):
        """Calculate and display total with discount"""
        if self.billDB.empty:
            subtotal = 0
        else:
            subtotal = (self.billDB['Price'] * self.billDB['Quantity']).sum()
        
        discount_amount = subtotal * (self.applied_discount / 100)
        total = subtotal - discount_amount
        
        total_text = f"Subtotal: ${subtotal:.2f}\n"
        if self.applied_discount > 0:
            total_text += f"Discount ({self.applied_discount}%): -${discount_amount:.2f}\n"
        total_text += f"Total: ${total:.2f}"
        
        self.total_label.config(text=total_text)

    def apply_discount(self):
        """Apply discount code if valid"""
        code = self.discount_entry.get().strip().upper()
        if code in self.discount_codes:
            self.applied_discount = self.discount_codes[code]
            messagebox.showinfo("Success", f"Discount code applied! {self.applied_discount}% off")
            self.discount_entry.delete(0, tk.END)
            self.update_total()
        else:
            messagebox.showerror("Error", "Invalid discount code")

    def save_bill(self):
        """Save the bill to CSV file with totals"""
        if self.billDB.empty:
            messagebox.showwarning("Warning", "Cart is empty")
            return
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"bill_{self.current_user}_{timestamp}.csv"
            
            bill_with_totals = self.billDB.copy()
            bill_with_totals['Total_Price'] = bill_with_totals['Price'] * bill_with_totals['Quantity']
            
            subtotal = bill_with_totals['Total_Price'].sum()
            discount_amount = subtotal * (self.applied_discount / 100)
            final_total = subtotal - discount_amount
            
            bill_with_totals.to_csv(filename, index=False)
            
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([])
                writer.writerow(['BILL SUMMARY'])
                writer.writerow(['User:', self.current_user])
                writer.writerow(['Date:', datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
                writer.writerow(['Subtotal:', f'${subtotal:.2f}'])
                writer.writerow(['Discount:', f'{self.applied_discount}%'])
                writer.writerow(['Discount Amount:', f'${discount_amount:.2f}'])
                writer.writerow(['Final Total:', f'${final_total:.2f}'])
            
            messagebox.showinfo("Success", f"Bill saved as {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bill: {str(e)}")

    def clear_cart(self):
        """Clear the shopping cart after confirmation"""
        if not self.billDB.empty:
            if messagebox.askyesno("Confirm", "Are you sure you want to clear the cart?"):
                self.billDB = pd.DataFrame(columns=["ProductID", "ProductName", "Category", "Price", "Quantity"])
                self.applied_discount = 0
                self.update_cart_display()

    def bind_mousewheel(self, event):
        self.products_canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
    def _on_mousewheel(self, event):
        self.products_canvas.yview_scroll(int(-1*(event.delta/120)), "units")



