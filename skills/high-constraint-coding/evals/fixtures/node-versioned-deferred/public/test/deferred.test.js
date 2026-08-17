import assert from "node:assert/strict";
import test from "node:test";

import { createDeferred } from "../src/deferred.js";

test("resolve fulfills the promise", async () => {
  const deferred = createDeferred();

  deferred.resolve("ready");

  await assert.doesNotReject(deferred.promise);
  assert.equal(await deferred.promise, "ready");
});

test("reject rejects the promise", async () => {
  const deferred = createDeferred();
  const error = new Error("failed");

  deferred.reject(error);

  await assert.rejects(deferred.promise, error);
});
