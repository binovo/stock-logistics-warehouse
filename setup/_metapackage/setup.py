import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-stock-logistics-warehouse",
    description="Meta package for oca-stock-logistics-warehouse Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_move_line_product>=16.0dev,<16.1dev',
        'odoo-addon-account_move_line_stock_info>=16.0dev,<16.1dev',
        'odoo-addon-base_product_merge>=16.0dev,<16.1dev',
        'odoo-addon-procurement_auto_create_group>=16.0dev,<16.1dev',
        'odoo-addon-product_packaging_usability>=16.0dev,<16.1dev',
        'odoo-addon-scrap_reason_code>=16.0dev,<16.1dev',
        'odoo-addon-stock_cycle_count>=16.0dev,<16.1dev',
        'odoo-addon-stock_demand_estimate>=16.0dev,<16.1dev',
        'odoo-addon-stock_demand_estimate_matrix>=16.0dev,<16.1dev',
        'odoo-addon-stock_exception>=16.0dev,<16.1dev',
        'odoo-addon-stock_helper>=16.0dev,<16.1dev',
        'odoo-addon-stock_inventory>=16.0dev,<16.1dev',
        'odoo-addon-stock_inventory_count_to_zero>=16.0dev,<16.1dev',
        'odoo-addon-stock_inventory_discrepancy>=16.0dev,<16.1dev',
        'odoo-addon-stock_inventory_justification>=16.0dev,<16.1dev',
        'odoo-addon-stock_inventory_preparation_filter>=16.0dev,<16.1dev',
        'odoo-addon-stock_location_lockdown>=16.0dev,<16.1dev',
        'odoo-addon-stock_location_package_restriction>=16.0dev,<16.1dev',
        'odoo-addon-stock_location_position>=16.0dev,<16.1dev',
        'odoo-addon-stock_location_product_restriction>=16.0dev,<16.1dev',
        'odoo-addon-stock_location_zone>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_auto_assign>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_auto_assign_auto_release>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_common_dest>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_location>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_packaging_qty>=16.0dev,<16.1dev',
        'odoo-addon-stock_mts_mto_rule>=16.0dev,<16.1dev',
        'odoo-addon-stock_package_type_category>=16.0dev,<16.1dev',
        'odoo-addon-stock_package_type_volume>=16.0dev,<16.1dev',
        'odoo-addon-stock_packaging_calculator>=16.0dev,<16.1dev',
        'odoo-addon-stock_packaging_calculator_packaging_level>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_packaging_qty>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_commercial_partner>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_procure_method>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_product_interchangeable>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_show_linked>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_volume>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_volume_packaging>=16.0dev,<16.1dev',
        'odoo-addon-stock_product_qty_by_packaging>=16.0dev,<16.1dev',
        'odoo-addon-stock_production_lot_quantity_tree>=16.0dev,<16.1dev',
        'odoo-addon-stock_pull_list>=16.0dev,<16.1dev',
        'odoo-addon-stock_putaway_product_template>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_cost_info>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_expiration_date_tree>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_manual_assign>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_reservation_info>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_reservation_info_mrp>=16.0dev,<16.1dev',
        'odoo-addon-stock_quant_safe_inventory>=16.0dev,<16.1dev',
        'odoo-addon-stock_removal_location_by_priority>=16.0dev,<16.1dev',
        'odoo-addon-stock_reservation_date_show>=16.0dev,<16.1dev',
        'odoo-addon-stock_reserve>=16.0dev,<16.1dev',
        'odoo-addon-stock_reserve_rule>=16.0dev,<16.1dev',
        'odoo-addon-stock_route_mto>=16.0dev,<16.1dev',
        'odoo-addon-stock_scrap_location_default>=16.0dev,<16.1dev',
        'odoo-addon-stock_search_supplierinfo_code>=16.0dev,<16.1dev',
        'odoo-addon-stock_secondary_unit>=16.0dev,<16.1dev',
        'odoo-addon-stock_storage_category_capacity_name>=16.0dev,<16.1dev',
        'odoo-addon-stock_valuation_layer_accounting_date>=16.0dev,<16.1dev',
        'odoo-addon-stock_valuation_layer_inventory_filter>=16.0dev,<16.1dev',
        'odoo-addon-stock_valuation_layer_total_value>=16.0dev,<16.1dev',
        'odoo-addon-stock_vlm_mgmt>=16.0dev,<16.1dev',
        'odoo-addon-stock_warehouse_calendar>=16.0dev,<16.1dev',
        'odoo-addon-stock_warehouse_relationship>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
