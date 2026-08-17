import assert from "node:assert/strict";
import test from "node:test";

import { createDeferred } from "../src/deferred.js";

test("exposes exactly a promise, resolve, and reject", () => {
  const deferred = createDeferred();

  assert.deepEqual(Object.keys(deferred).sort(), ["promise", "reject", "resolve"]);
  assert.ok(deferred.promise instanceof Promise);
  assert.equal(typeof deferred.resolve, "function");
  assert.equal(typeof deferred.reject, "function");
});

test("the first terminal call wins", async (t) => {
  await t.test("resolve before reject remains fulfilled", async () => {
    const deferred = createDeferred();

    deferred.resolve("first");
    deferred.reject(new Error("second"));

    assert.equal(await deferred.promise, "first");
  });

  await t.test("reject before resolve remains rejected", async () => {
    const deferred = createDeferred();
    const error = new Error("first");

    deferred.reject(error);
    deferred.resolve("second");

    await assert.rejects(deferred.promise, error);
  });
});

test("instances settle independently", async () => {
  const first = createDeferred();
  const second = createDeferred();
  const error = new Error("second");

  first.resolve("first");
  second.reject(error);

  assert.equal(await first.promise, "first");
  await assert.rejects(second.promise, error);
});
