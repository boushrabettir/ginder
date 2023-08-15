export let final_response: string = '';

const case_0: string[] = [
	'What an eye-catching small project!🌟👀',
	'A small project that truly stands out!🔥👌',
	'Impressive in its smallness!🎉🔍',
	'Small but mighty!✨🚀',
	'This small project packs a punch!🌈👏',
	'A gem of a small project!💎🔮',
	'Exceeding expectations in its smallness!🌠🚀',
	'An eye-catcher, even in its small form!🌺🔑',
	'Small size, huge impact!🎯💥',
	'What a delightfully small project!🚀🌱',
	'What an eye-catching small project!💥🌐'
];

const case_1: string[] = [
	'This project has taken the internet by storm!💥🌐',
	'Witness the wildfire spread of this viral project!🔥🌍',
	"A viral sensation that's capturing everyone's attention!🌟🚀",
	'Exploding onto the scene with viral magnificence!🚀🔥',
	"A project that's breaking the internet's popularity meter!📈🔥",
	'From zero to viral hero in no time!🚀🔥',
	'This project is setting the internet ablaze with its virality!🔥🌐',
	'Catching fire online with unstoppable viral momentum!🔥🚀',
	'A whirlwind of viral success sweeping across the web!🌪️🔥',
	"A viral phenomenon that's leaving everyone in awe!🔥🌟",
	"Talk about a project that's totally gone viral!💯🔥"
];

const case_2: string[] = [
	'Celebrating an incredible 10k stargazers - a monumental achievement! 🚀🌟',
	'10k stargazers have propelled this project to astounding heights! 🌌🚀',
	'With 10k stargazers, the impact of this achievement is undeniable! 🌟🚀',
	'An applause-worthy feat: 10k stargazers supporting the journey! 🎉🚀',
	"The mark of 10k stargazers - a testament to the project's allure! 🌟🚀",
	"Here's to the magic of 10k stargazers who've embraced this project! ✨🚀",
	'Reaching 10k stargazers - a remarkable milestone for this endeavor! 🌟🚀',
	'A standing ovation for the achievement of 10k stargazers! 🎉🚀',
	'10k stargazers shining bright on this remarkable path! 🌟🚀',
	"The journey to 10k stargazers is etched in the stars of this project's story! ✨🚀",
	'There are over 10k stargazers...this project is off the moon!🚀🌙⭐'
];

/**
 * determine_message determines which message to be given
 * based on the number of stargazers
 */
export const determine_message = (stargazers: number): string => {
	switch (Math.floor(stargazers / 5000)) {
		case 0:
			final_response = case_0[Math.floor(Math.random() * case_0.length)];
			break;
		case 1:
			final_response = case_1[Math.floor(Math.random() * case_1.length)];
			break;
		case 2:
			final_response = case_2[Math.floor(Math.random() * case_2.length)];
			break;
		default:
			final_response = case_2[Math.floor(Math.random() * case_2.length)];
			break;
	}

	return final_response;
};
