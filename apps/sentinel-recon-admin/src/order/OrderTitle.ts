import { Order as TOrder } from "../api/order/Order";

export const ORDER_TITLE_FIELD = "username";

export const OrderTitle = (record: TOrder): string => {
  return record.username || String(record.id);
};
