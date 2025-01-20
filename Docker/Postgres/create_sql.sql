-- -----------------------------------------------------
-- Table public.customer
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.customer
(
    id BIGINT,
    company TEXT,
    last_name TEXT,
    first_name TEXT,
    email_address TEXT,
    job_title TEXT,
    business_phone TEXT,
    home_phone TEXT,
    mobile_phone TEXT,
    fax_number TEXT,
    address TEXT,
    city TEXT,
    state_province TEXT,
    zip_postal_code TEXT,
    country_region TEXT,
    web_page TEXT,
    notes TEXT,
    attachments TEXT
);
ALTER TABLE public.customer OWNER TO sa;

-- -----------------------------------------------------
-- Table public.employees
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.employees
(
    id BIGINT,
    company TEXT,
    last_name TEXT,
    first_name TEXT,
    email_address TEXT,
    job_title TEXT,
    business_phone TEXT,
    home_phone TEXT,
    mobile_phone TEXT,
    fax_number TEXT,
    address TEXT,
    city TEXT,
    state_province TEXT,
    zip_postal_code TEXT,
    country_region TEXT,
    web_page TEXT,
    notes TEXT,
    attachments TEXT
);
ALTER TABLE public.employees OWNER TO sa;

-- -----------------------------------------------------
-- Table public.privileges
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.privileges
(
    id BIGINT,
    privilege_name TEXT
);
ALTER TABLE public.privileges OWNER TO sa;

-- -----------------------------------------------------
-- Table public.employee_privileges
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.employee_privileges
(
    employee_id BIGINT,
    privilege_id BIGINT
);
ALTER TABLE public.employee_privileges OWNER TO sa;

-- -----------------------------------------------------
-- Table public.inventory_transaction_types
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.inventory_transaction_types
(
    id BIGINT,
    type_name TEXT
);
ALTER TABLE public.inventory_transaction_types OWNER TO sa;

-- -----------------------------------------------------
-- Table public.shippers
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.shippers
(
    id BIGINT,
    company TEXT,
    last_name TEXT,
    first_name TEXT,
    email_address TEXT,
    job_title TEXT,
    business_phone TEXT,
    home_phone TEXT,
    mobile_phone TEXT,
    fax_number TEXT,
    address TEXT,
    city TEXT,
    state_province TEXT,
    zip_postal_code TEXT,
    country_region TEXT,
    web_page TEXT,
    notes TEXT,
    attachments TEXT
);
ALTER TABLE public.shippers OWNER TO sa;

-- -----------------------------------------------------
-- Table public.orders_tax_status
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.orders_tax_status
(
    id BIGINT,
    tax_status_name TEXT
);
ALTER TABLE public.orders_tax_status OWNER TO sa;

-- -----------------------------------------------------
-- Table public.orders_status
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.orders_status
(
    id BIGINT,
    status_name TEXT
);
ALTER TABLE public.orders_status OWNER TO sa;

-- -----------------------------------------------------
-- Table public.orders
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.orders
(
    id BIGINT,
    employee_id BIGINT,
    customer_id BIGINT,
    order_date TIMESTAMP,
    shipped_date TIMESTAMP,
    shipper_id BIGINT,
    ship_name TEXT,
    ship_address TEXT,
    ship_city TEXT,
    ship_state_province TEXT,
    ship_zip_postal_code TEXT,
    ship_country_region TEXT,
    shipping_fee NUMERIC,
    taxes NUMERIC,
    payment_type TEXT,
    paid_date TIMESTAMP,
    notes TEXT,
    tax_rate NUMERIC,
    tax_status_id BIGINT,
    status_id BIGINT
);
ALTER TABLE public.orders OWNER TO sa;

-- -----------------------------------------------------
-- Table public.products
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.products
(
    supplier_ids TEXT,
    id BIGINT,
    product_code TEXT,
    product_name TEXT,
    description TEXT,
    standard_cost NUMERIC,
    list_price NUMERIC,
    reorder_level BIGINT,
    target_level BIGINT,
    quantity_per_unit TEXT,
    discontinued BIGINT,
    minimum_reorder_quantity BIGINT,
    category TEXT,
    attachments TEXT
);
ALTER TABLE public.products OWNER TO sa;

-- -----------------------------------------------------
-- Table public.purchase_order_status
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.purchase_order_status
(
    id BIGINT,
    status TEXT
);
ALTER TABLE public.purchase_order_status OWNER TO sa;

-- -----------------------------------------------------
-- Table public.suppliers
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.suppliers
(
    id BIGINT,
    company TEXT,
    last_name TEXT,
    first_name TEXT,
    email_address TEXT,
    job_title TEXT,
    business_phone TEXT,
    home_phone TEXT,
    mobile_phone TEXT,
    fax_number TEXT,
    address TEXT,
    city TEXT,
    state_province TEXT,
    zip_postal_code TEXT,
    country_region TEXT,
    web_page TEXT,
    notes TEXT,
    attachments TEXT
);
ALTER TABLE public.suppliers OWNER TO sa;

-- -----------------------------------------------------
-- Table public.purchase_orders
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.purchase_orders
(
    id BIGINT,
    supplier_id BIGINT,
    created_by BIGINT,
    submitted_date TIMESTAMP,
    creation_date TIMESTAMP,
    status_id BIGINT,
    expected_date TIMESTAMP,
    shipping_fee NUMERIC,
    taxes NUMERIC,
    payment_date TIMESTAMP,
    payment_amount NUMERIC,
    payment_method TEXT,
    notes TEXT,
    approved_by BIGINT,
    approved_date TIMESTAMP,
    submitted_by BIGINT
);
ALTER TABLE public.purchase_orders OWNER TO sa;

-- -----------------------------------------------------
-- Table public.inventory_transactions
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.inventory_transactions
(
    id BIGINT,
    transaction_type BIGINT,
    transaction_created_date TIMESTAMP,
    transaction_modified_date TIMESTAMP,
    product_id BIGINT,
    quantity BIGINT,
    purchase_order_id BIGINT,
    customer_order_id BIGINT,
    comments TEXT
);
ALTER TABLE public.inventory_transactions OWNER TO sa;

-- -----------------------------------------------------
-- Table public.invoices
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.invoices
(
    id BIGINT,
    order_id BIGINT,
    invoice_date TIMESTAMP,
    due_date TIMESTAMP,
    tax NUMERIC,
    shipping NUMERIC,
    amount_due NUMERIC
);
ALTER TABLE public.invoices OWNER TO sa;

-- -----------------------------------------------------
-- Table public.order_details_status
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.order_details_status
(
    id BIGINT,
    status TEXT
);
ALTER TABLE public.order_details_status OWNER TO sa;

-- -----------------------------------------------------
-- Table public.order_details
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.order_details
(
    id BIGINT,
    order_id BIGINT,
    product_id BIGINT,
    quantity NUMERIC,
    unit_price NUMERIC,
    discount NUMERIC,
    status_id BIGINT,
    date_allocated TIMESTAMP,
    purchase_order_id BIGINT,
    inventory_id BIGINT
);
ALTER TABLE public.order_details OWNER TO sa;

-- -----------------------------------------------------
-- Table public.purchase_order_details
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.purchase_order_details
(
    id BIGINT,
    purchase_order_id BIGINT,
    product_id BIGINT,
    quantity NUMERIC,
    unit_cost NUMERIC,
    date_received TIMESTAMP,
    posted_to_inventory BIGINT,
    inventory_id BIGINT
);
ALTER TABLE public.purchase_order_details OWNER TO sa;

-- -----------------------------------------------------
-- Table public.sales_reports
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.sales_reports
(
    group_by TEXT,
    display TEXT,
    title TEXT,
    filter_row_source TEXT,
    defaulted TEXT
);
ALTER TABLE public.sales_reports OWNER TO sa;

-- -----------------------------------------------------
-- Table public.strings
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.strings
(
    string_id BIGINT,
    string_data TEXT
);
ALTER TABLE public.strings OWNER TO sa;
