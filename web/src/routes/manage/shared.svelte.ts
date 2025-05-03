export const currentTab: {
	tab: 'replacements' | 'timetables' | 'groups' | 'subjects' | 'teachers';
} = $state({
	tab: 'replacements' // sadly, an exported state must be an object , because you cannot assign to exported variables
});
