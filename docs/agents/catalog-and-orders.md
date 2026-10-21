---
title: Catalog & order taking
summary: Let an agent answer questions about your products and take orders, and what each catalog switch does.
tags:
  - agents
  - catalog
  - orders
  - configuration
keywords:
  - menu
  - catalog
  - order taking
  - prices
  - quantity
  - add-ons
  - availability
help_key: agents.catalog
help_keys:
  - agents.order_taking
  - agents.show_prices
  - agents.ask_quantity
  - agents.item_available
  - agents.addon_required
---

# Catalog & order taking

An agent can know your products and take orders on the call. This card appears on the
agent page only when a super-admin has turned on
[Order taking for your operator](../admin.md#order-taking-enabled).

## Catalog / product info {#catalog}

Turn this on and the agent answers questions about your items, prices and what is
available, using the menu you build below the switch. It works **without** order
taking, so you can use it as a product guide only.

When the switch is off the agent does not know the menu, and order taking is switched
off too (it needs the catalog).

## Order taking {#order-taking}

Turn this on (the catalog must be on first) and the agent takes an order during the
call: it checks each item against the menu, asks for sizes and add-ons, and records the
order. Every finished order is emailed to the **Order notification email** you set
in the menu editor.

If order taking is not available on the platform at that moment, the agent simply
carries on without it; the call does not fail.

!!! info "Cost"
    The menu is added to what the agent reads, so a very large menu makes each call a
    little heavier. The editor warns you when a catalog is large.

## Show prices to callers {#show-prices}

On by default. Turn it **off** to keep prices out of the call completely: the agent
will not quote or discuss them, even if asked, and says pricing is not available over
the phone. You can still keep prices in the menu for your own records.

## Ask quantity for every item {#ask-quantity}

When **on**, the agent always asks how many before adding an item. When **off**, it
assumes one unless the caller says a number. Turn it on for items people usually
order in numbers (tickets, pastries).

## Item available {#item-available}

Each item has an **Available** switch. An item that is **off** is left out of what the
agent knows, so it will not offer it or take it in an order. The item stays in your
catalog; switch it back on when it is in stock again.

## Add-on group: Required {#addon-required}

An add-on group (toppings, sauces, sizes of side) is either **Pick one** or **Pick
any**. Tick **Required** and the agent must get a choice from that group before the item
is added: one choice for "Pick one", at least one for "Pick any". Leave it unticked and
the add-on is optional.

## Related

- Turning order taking on for an operator → [Administration](../admin.md#operator-switches)
