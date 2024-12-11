import { Field, ObjectType } from "@nestjs/graphql";
import { Order } from "../order/base/Order";

@ObjectType()
export class OrderInfo implements Partial<Order> {
  @Field(() => String)
  id!: string;
  @Field(() => String)
  username!: string;
  @Field(() => [String])
  roles!: string[];
  @Field(() => String, { nullable: true })
  accessToken?: string;
}
