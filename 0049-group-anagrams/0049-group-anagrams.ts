function groupAnagrams(strs: string[]): string[][] {
    const anagramList: string[][] = [];

    function sortString(str: string): string {
        return str.split('').sort().join('');
    }

    const anagramMap = new Map<string, string[]>();

    for (const str of strs) {
        const sortedStr = sortString(str);
        const anagramGroup = anagramMap.get(sortedStr) || [];
        anagramGroup.push(str);
        anagramMap.set(sortedStr, anagramGroup);
    }

    for (const group of anagramMap.values()) {
        anagramList.push(group);
    }

    return anagramList;
}