from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order


class Trader:
	def __init__(self):
		self.gains = 0
		# self.prev = []
		# self.average = 0
		
	def run(self, state: TradingState) -> Dict[str, List[Order]]:
		"""
		Only method required. It takes all buy and sell orders for all symbols as an input,
		and outputs a list of orders to be sent
		"""
		# Initialize the method output dict as an empty dict
		result = {}
	
		# Iterate over all the keys (the available products) contained in the order depths
		for product in state.order_depths.keys():
			# Check if the current product is the 'PEARLS' product, only then run the order logic
			if product == 'PEARLS':
				# print("Position:", state.position)
				# Retrieve the Order Depth containing all the market BUY and SELL orders for PEARLS
				order_depth: OrderDepth = state.order_depths[product]

				# Initialize the list of Orders to be sent as an empty list
				orders: list[Order] = []

				# Define a fair value for the PEARLS.
				# Note that this value of 1 is just a dummy value, you should likely change it!
				acceptable_price = 10000
				best_ask = min(order_depth.sell_orders.keys())
				best_ask_volume = order_depth.sell_orders[best_ask]
				best_bid = max(order_depth.buy_orders.keys())
				best_bid_volume = order_depth.buy_orders[best_bid]
				# average = (best_ask*-best_ask_volume + best_bid+best_bid_volume)/(-best_ask_volume+best_bid_volume)
				# self.prev
				print("Position:", state.position)
				print("Position:", state.position.PEARLS)
				print("BBO:", best_bid, best_ask)
				
				# If statement checks if there are any SELL orders in the PEARLS market
				if len(order_depth.sell_orders) > 0:

					# Check if the lowest ask (sell order) is lower than the above defined fair value
					if best_ask < acceptable_price:

						# if (state.position['PEARLS']-best_ask_volume>20):
						# 	best_ask_volume = 20-state.position['PEARLS'] 
						# 	best_ask_volume *= -1
						self.gains += best_ask_volume*best_ask
						print("BUY", str(-best_ask_volume) + "x", best_ask, "Gains:", self.gains)
						orders.append(Order(product, best_ask, -best_ask_volume))
						

				# The below code block is similar to the one above,
				# the difference is that it finds the highest bid (buy order)
				# If the price of the order is higher than the fair value
				# This is an opportunity to sell at a premium

				if len(order_depth.buy_orders) > 0:


					if best_bid > acceptable_price:
						# if (state.position['PEARLS']-best_bid_volume < 0):
						# 	best_bid_volume = state.position['PEARLS'] 
						self.gains += best_bid_volume*best_bid
						print("SELL", str(best_bid_volume) + "x", best_bid, "Gains:", self.gains)
						orders.append(Order(product, best_bid, -best_bid_volume))
				
				print("BBO:", best_bid, best_ask)
				# Add all the above orders to the result dict
				result[product] = orders

				# Return the dict of orders
				# These possibly contain buy or sell orders for PEARLS
				# Depending on the logic above
		return result