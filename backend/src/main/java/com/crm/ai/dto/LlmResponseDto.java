package com.crm.ai.dto;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class LlmResponseDto {
    private String response;
    private String model;
    
    @com.fasterxml.jackson.annotation.JsonProperty("ppt_file_path")
    private String pptFilePath;
    
    @com.fasterxml.jackson.annotation.JsonProperty("ppt_file_name")
    private String pptFileName;
    
    private String status;
}
