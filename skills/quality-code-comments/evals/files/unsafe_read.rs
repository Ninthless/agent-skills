pub unsafe fn read_u16_le(ptr: *const u8) -> u16 {
    let bytes = [unsafe { *ptr }, unsafe { *ptr.add(1) }];
    u16::from_le_bytes(bytes)
}
