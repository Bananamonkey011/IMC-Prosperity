from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order


class Trader:
	def __init__(self):
		self.gains = 0
		self.prev_pearls = []
		self.prev_pearls_ask = []
		self.prev_pearls_bid = []
		self.prev_bananas = []
		self.bananas_position = (0,0)
		self.bap = 0
		self.bbp = 0
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
			# if product == 'PEARLS':
			# 	# print("Position:", state.position)
			# 	# Retrieve the Order Depth containing all the market BUY and SELL orders for PEARLS
			# 	order_depth: OrderDepth = state.order_depths[product]

			# 	# Initialize the list of Orders to be sent as an empty list
			# 	orders: list[Order] = []

			# 	# Define a fair value for the PEARLS.
			# 	# Note that this value of 1 is just a dummy value, you should likely change it!
			# 	best_ask = min(order_depth.sell_orders.keys())
			# 	best_ask_volume = -order_depth.sell_orders[best_ask]
			# 	best_bid = max(order_depth.buy_orders.keys())
			# 	best_bid_volume = order_depth.buy_orders[best_bid]
			# 	average = (best_ask*best_ask_volume + best_bid*best_bid_volume)/(best_ask_volume+best_bid_volume)
				
			# 	self.prev_pearls.append(average)
			# 	self.prev_pearls_ask.append(best_ask)
			# 	self.prev_pearls_bid.append(best_bid)
			# 	if len(self.prev_pearls) > 20:
			# 		self.prev_pearls.pop(0)
			# 		self.prev_pearls_ask.pop(0)
			# 		self.prev_pearls_bid.pop(0)
			# 		acceptable_price = sum(self.prev_pearls)/len(self.prev_pearls)
			# 		acceptable_ask = sum(self.prev_pearls_ask)/len(self.prev_pearls_ask)
			# 		acceptable_bid = sum(self.prev_pearls_bid)/len(self.prev_pearls_bid)
			# 	else:
			# 		acceptable_price = acceptable_ask = acceptable_bid = 10000

			# 	print("Pearl Position:", state.position.get(product, 0))
			# 	print("BBO:", best_bid, best_ask)
			# 	print("acceptable_prices (ask) (bid):", acceptable_ask, acceptable_bid)
			# 	max_position_value_sell = 20
			# 	max_position_value_buy = 20

			# 	# If statement checks if there are any SELL orders in the PEARLS market
			# 	if len(order_depth.sell_orders) > 0:

			# 		# Check if the lowest ask (sell order) is lower than the above defined fair value
			# 		if best_ask < acceptable_ask:

			# 			if (state.position.get(product, 0)+best_ask_volume>max_position_value_sell):
			# 				best_ask_volume = max_position_value_sell-state.position.get(product, 0)

			# 			self.gains -= best_ask_volume*best_ask
			# 			print("BUY", str(best_ask_volume) + "x", best_ask, "Gains:", self.gains)
			# 			orders.append(Order(product, best_ask, best_ask_volume))
			# 			#max_position_value_buy = min(max_position_value_buy, best_ask_volume)
						

			# 	if len(order_depth.buy_orders) > 0:
			# 		if best_bid > acceptable_bid:
			# 			if (state.position.get(product, 0)-best_bid_volume < -max_position_value_buy):
			# 				best_bid_volume = state.position.get(product, 0)
							
			# 			self.gains += best_bid_volume*best_bid
			# 			print("SELL", str(best_bid_volume) + "x", best_bid, "Gains:", self.gains)
			# 			orders.append(Order(product, best_bid, -best_bid_volume))
			# 			#max_position_value_sell = min(max_position_value_sell, best_bid_volume)
				

			# 	# Add all the above orders to the result dict
			# 	result[product] = orders
			
		# 	if product == 'BANANAS':
		# 		# print("Position:", state.position)
		# 		# Retrieve the Order Depth containing all the market BUY and SELL orders for PEARLS
		# 		order_depth: OrderDepth = state.order_depths[product]

		# 		# Initialize the list of Orders to be sent as an empty list
		# 		orders: list[Order] = []

		# 		# Define a fair value for the PEARLS.
		# 		# Note that this value of 1 is just a dummy value, you should likely change it!
		# 		best_ask = min(order_depth.sell_orders.keys())
		# 		best_ask_volume = -order_depth.sell_orders[best_ask]
		# 		best_bid = max(order_depth.buy_orders.keys())
		# 		best_bid_volume = order_depth.buy_orders[best_bid]
		# 		#average = (best_ask*best_ask_volume + best_bid*best_bid_volume)/(best_ask_volume+best_bid_volume)
		# 		self.prev_bananas.append(average)
		# 		if len(self.prev_bananas) > 50: #self.bananas_position[1] != 0:
		# 			self.prev_bananas.pop(0)
		# 			acceptable_price = sum(self.prev_bananas)/len(self.prev_bananas)#self.bananas_position[1] 
		# 		else:
		# 			acceptable_price = 4900

		# 		print("Banana Position:", state.position.get(product, 0))
		# 		print("BBO:", best_bid, best_ask)
		# 		print("acceptable_price:", acceptable_price)
		# 		max_position_value_sell = 20
		# 		max_position_value_buy = 20


		# 		# If statement checks if there are any SELL orders in the PEARLS market
		# 		if len(order_depth.sell_orders) > 0:

		# 			# Check if the lowest ask (sell order) is lower than the above defined fair value
		# 			if best_ask < acceptable_price:

		# 				if (state.position.get(product, 0)+best_ask_volume>max_position_value_sell):
		# 					best_ask_volume = max_position_value_sell-state.position.get(product, 0)

		# 				self.gains -= best_ask_volume*best_ask
		# 				print("BUY", str(best_ask_volume) + "x", best_ask, "Gains:", self.gains)
		# 				orders.append(Order(product, best_ask, best_ask_volume))
		# 				#a,b = self.bananas_position
		# 				#self.bananas_position = (a + best_ask_volume, (a*b + best_ask_volume*best_ask) / (a+best_ask_volume))

		# 		if len(order_depth.buy_orders) > 0:


		# 			if best_bid > acceptable_price:
		# 				if (state.position.get(product, 0)-best_bid_volume < -max_position_value_buy):
		# 					best_bid_volume = state.position.get(product, 0)
							
		# 				self.gains += best_bid_volume*best_bid
		# 				print("SELL", str(best_bid_volume) + "x", best_bid, "Gains:", self.gains)
		# 				orders.append(Order(product, best_bid, -best_bid_volume))
		# 				# a,b = self.bananas_position
		# 				# if a-best_bid_volume != 0:
		# 				# 	self.bananas_position = (a - best_bid_volume, (a*b - best_bid_volume*best_bid) / (a-best_bid_volume))
		# 				# else:
		# 				# 	self.bananas_position = (0,b)
		# 				#max_position_value_sell = min(max_position_value_sell, best_bid_volume)
				

		# 		# Add all the above orders to the result dict
		# 		result[product] = orders
		# 	# elif product == 'BANANAS':
		# 		# Return the dict of orders
		# 		# These possibly contain buy or sell orders for PEARLS
		# 		# Depending on the logic above
		# return result

		if product == 'BANANAS':
				# print("Position:", state.position)
				# Retrieve the Order Depth containing all the market BUY and SELL orders for PEARLS
				order_depth: OrderDepth = state.order_depths[product]

				# Initialize the list of Orders to be sent as an empty list
				orders: list[Order] = []

				# Define a fair value for the PEARLS.
				# Note that this value of 1 is just a dummy value, you should likely change it!
				best_ask = min(order_depth.sell_orders.keys())
				best_ask_volume = -order_depth.sell_orders[best_ask]
				best_bid = max(order_depth.buy_orders.keys())
				best_bid_volume = order_depth.buy_orders[best_bid]
				


				print("Banana Position:", state.position.get(product, 0))
				print("BBO:", best_bid, best_ask)
				print("acceptable_price:", acceptable_price)
				

				if len(order_depth.sell_orders) > 0:
					if best_ask > self.bap:
						if (state.position.get(product, 0)+best_ask_volume>20):
							best_ask_volume = 20-state.position.get(product, 0)

						self.gains -= best_ask_volume*best_ask
						print("BUY", str(best_ask_volume) + "x", best_ask, "Gains:", self.gains)
						orders.append(Order(product, best_ask, best_ask_volume))

				if len(order_depth.buy_orders) > 0:
					if best_bid < self.bbp:
						if (state.position.get(product, 0)-best_bid_volume < -20):
							best_bid_volume = state.position.get(product, 0)
						self.gains += best_bid_volume*best_bid
						print("SELL", str(best_bid_volume) + "x", best_bid, "Gains:", self.gains)
						orders.append(Order(product, best_bid, -best_bid_volume))

				self.bap = best_ask
				self.bbp = best_bid
				result[product] = orders
		return result