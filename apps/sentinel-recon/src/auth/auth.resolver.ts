import * as common from "@nestjs/common";
import { Args, Mutation, Query, Resolver } from "@nestjs/graphql";
import * as gqlACGuard from "../auth/gqlAC.guard";
import { AuthService } from "./auth.service";
import { GqlDefaultAuthGuard } from "./gqlDefaultAuth.guard";
import { UserData } from "./userData.decorator";
import { LoginArgs } from "./LoginArgs";
import { OrderInfo } from "./OrderInfo";

@Resolver(OrderInfo)
export class AuthResolver {
  constructor(private readonly authService: AuthService) {}
  @Mutation(() => OrderInfo)
  async login(@Args() args: LoginArgs): Promise<OrderInfo> {
    return this.authService.login(args.credentials);
  }

  @Query(() => OrderInfo)
  @common.UseGuards(GqlDefaultAuthGuard, gqlACGuard.GqlACGuard)
  async orderInfo(@UserData() entityInfo: OrderInfo): Promise<OrderInfo> {
    return entityInfo;
  }
}
