import { OrderInfo } from "./OrderInfo";

export interface IAuthStrategy {
  validate: (...any: any) => Promise<OrderInfo>;
}
