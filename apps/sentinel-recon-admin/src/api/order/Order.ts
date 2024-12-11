import { Customer } from "../customer/Customer";
import { Product } from "../product/Product";
import { JsonValue } from "type-fest";

export type Order = {
  createdAt: Date;
  customer?: Customer | null;
  discount: number | null;
  id: string;
  product?: Product | null;
  quantity: number | null;
  totalPrice: number | null;
  updatedAt: Date;
  username: string;
  roles: JsonValue;
};
