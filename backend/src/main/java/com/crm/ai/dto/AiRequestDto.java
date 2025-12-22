package com.crm.ai.dto;

import lombok.Data;
import java.util.Map;

@Data
public class AiRequestDto {
    private String intent;
    private String query;
    private Map<String, String> filters;
}
