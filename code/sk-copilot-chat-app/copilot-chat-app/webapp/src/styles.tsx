import { BrandVariants, GriffelStyle, createLightTheme, tokens } from '@fluentui/react-components';

const semanticKernelBrandRamp: BrandVariants = {
    10: "#060103",
    20: "#261018",
    30: "#431426",
    40: "#591732",
    50: "#701A3E",
    60: "#861F4B",
    70: "#982C57",
    80: "#A53E63",
    90: "#B15070",
    100: "#BC627E",
    110: "#C6748B",
    120: "#CF869A",
    130: "#D898A8",
    140: "#E0AAB7",
    150: "#E8BCC6",
    160: "#EFCFD6"
};

export const semanticKernelLightTheme = createLightTheme(semanticKernelBrandRamp);

export const Breakpoints = {
    small: (style: GriffelStyle): Record<string, GriffelStyle> => {
        return { '@media (max-width: 744px)': style };
    },
};

export const SharedStyles: Record<string, GriffelStyle> = {
    scroll: {
        overflowY: 'scroll',
        '&:hover': {
            '&::-webkit-scrollbar-thumb': {
                backgroundColor: tokens.colorScrollbarOverlay,
                visibility: 'visible',
            },
            '&::-webkit-scrollbar-track': {
                backgroundColor: tokens.colorNeutralBackground1,
                WebkitBoxShadow: 'inset 0 0 5px rgba(0, 0, 0, 0.1)',
                visibility: 'visible',
            },
        },
        height: '100%',
    },
};
