import { useRef, useState } from "react";

interface Props {
  direction: "vertical" | "horizontal";
  // Called while dragging, with the pointer's position (x for vertical, y for horizontal).
  onMove: (position: number) => void;
  label: string;
}

export default function Splitter({ direction, onMove, label }: Props) {
  const [dragging, setDragging] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  return (
    <div
      ref={ref}
      className={`${direction === "vertical" ? "split-v" : "split-h"}${dragging ? " drag" : ""}`}
      role="separator"
      aria-orientation={direction}
      aria-label={label}
      onPointerDown={(e) => {
        ref.current?.setPointerCapture(e.pointerId);
        setDragging(true);
        document.body.style.userSelect = "none";
      }}
      onPointerMove={(e) => {
        if (dragging) onMove(direction === "vertical" ? e.clientX : e.clientY);
      }}
      onPointerUp={(e) => {
        ref.current?.releasePointerCapture(e.pointerId);
        setDragging(false);
        document.body.style.userSelect = "";
      }}
    />
  );
}
