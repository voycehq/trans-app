import Select from "react-select";
import { colors } from "../libs/utils";

const filteStyle = {
  control: (style: any) => ({
    ...style,
    backgroundColor: colors.hover_color,
    display: "grid",
    gridTemplateColumns: "1fr min-content",
    alignContent: "center",
    border: colors.border,
    outline: "none",
    height: "30px",
    minHeight: "25px",
    width: "100%",
    minWidth: "8rem",
    transition: "unset",
    cursor: "pointer",
  }),
  singleValue: (style: any) => ({
    ...style,
    color: colors.primary_color,
  }),
  option: (style: any) => ({
    ...style,
    cursor: "pointer",
  }),
  // placeholder: (style: any) => ({
  //   ...style,
  //   position: "relative",
  //   top: "0",
  //   transform: "none",
  //   color: colors.white_color,
  //   fontSize: "13px",
  //   overflow: "unset",
  // }),
  // valueContainer: (style: any) => ({
  //   ...style,
  //   flexWrap: "nowrap",
  //   padding: "2px 4px 2px 6px",
  //   alignItems: "center",
  // }),
  // indicatorSeparator: (style: any) => ({
  //   ...style,
  //   backgroundColor: colors.white_color,
  // }),
  // input: (style: any) => ({
  //   ...style,
  //   color: colors.white_color,
  //   fontSize: "13px",
  // }),
  // menu: (style: any) => ({
  //   ...style,
  //   width: "100%",
  //   minWidth: "100px",
  //   fontSize: "13px",
  // }),
};
interface Options {
  value: string;
  label: string;
}
interface Props {
  options: Options[];
  value: Options[];
  onChange: any;
  id: string;
  defaultValue?: Options[];
  palceholder?: string;
  width?: string;
  isClearable?: boolean;
}

const SelectMenu = ({
  options,
  value,
  defaultValue,
  onChange,
  id,
  palceholder,
  width = "fit-content",
  isClearable = true,
}: Props): JSX.Element => {
  return (
    <div style={{ width }}>
      <Select
        instanceId={id}
        defaultValue={defaultValue}
        value={value}
        onChange={onChange}
        styles={filteStyle}
        isClearable={isClearable}
        theme={(theme) => ({
          ...theme,
          colors: {
            ...theme.colors,
            primary25: colors.grey,
            primary: colors.primary_color,
          },
        })}
        options={options}
        isSearchable={false}
        isMulti={false}
        placeholder={palceholder}
      />
    </div>
  );
};

export default SelectMenu;
