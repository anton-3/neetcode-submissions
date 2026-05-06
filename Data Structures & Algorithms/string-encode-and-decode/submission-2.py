class Solution:
    MAX_STRING_LEN = 3

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            len_str = str(len(s)).zfill(self.MAX_STRING_LEN)
            encoded_str = f'{len_str}{s}'
            encoded.append(encoded_str)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            try:
                s_part_idx = i + self.MAX_STRING_LEN
                s_len = int(s[i:s_part_idx])
                s_part = s[s_part_idx:s_part_idx+s_len]
                decoded.append(s_part)
                i += self.MAX_STRING_LEN + len(s_part)
            except:
                raise ValueError('Invalid string encoding')
        return decoded
